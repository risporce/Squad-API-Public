import socket
from LogicSquadMessageFactory import LogicSquadMessageFactory
from Crypto import Crypto
import threading
import queue
from Packets.PiranhaMessage import PiranhaMessage
import time
import traceback
from Packets.Server.PlayerProfileMessage import PlayerProfileMessage
from Packets.Server.LeaderboardDataMessage import LeaderboardDataMessage
import re
from Packets.PacketsEnum import LogicSquadPackets
from ClientGlobals import Configs



class APIClient:
    def __init__(self, configs: Configs, logicData, account: dict):
        self.host = configs.global_data.server.server
        self.port = configs.global_data.server.port
        self.logicData = logicData
        self.socket = None
        self.cryptoinit = Crypto(configs.global_data.server.server_public_key)
        self.packet_queue = queue.Queue()
        self.running = False
        self.stop_signal = False
        self.leaderboard_stop_signal = False
        self.local_leaderboard_stop_signal = False
        self.returningMessage : PlayerProfileMessage = None
        self.leaderboardData : LeaderboardDataMessage = None
        self.localLeaderboardData : LeaderboardDataMessage = None
        self.user_id : str = ""
        self.listener_thread = None
        self.account = account

        self.keep_alive_thread = None

    def recvall(self, lenght: int) -> bytes:
        data = b''
        while len(data) < lenght:
            s = self.socket.recv(lenght)
            data += s
        return data

    def connecting(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.running = True
        self.sendMessage(LogicSquadPackets.CLIENT_HELLO_MESSAGE.value)
        self.listener_thread = threading.Thread(target = self.listen_for_messages)
        self.listener_thread.start()
        self.keep_alive_thread = threading.Thread(target=self.activate_send_keep_alive, daemon=True)
        self.keep_alive_thread.start()



    def sendMessage(self, packet_id):
        fields = {}
        if packet_id == LogicSquadPackets.LOGIN_MESSAGE.value:
            fields["h"] = self.account.get("h")
            fields["l"] = self.account.get("l")
            fields["p"] = self.account.get("p")
        if packet_id == LogicSquadPackets.ASK_PLAYER_PROFILE_MESSAGE.value:
            user_id : list[str, str] = self.user_id.split("-")
            fields["high"] = int(user_id[0])
            fields["low"] = int(user_id[1])
        fields["Status"] = False
        message: PiranhaMessage = LogicSquadMessageFactory.createMessageByType(packet_id, b'', self.logicData)
        message.encode(fields=fields)
        message.messagePayload = self.cryptoinit.encryptClient(packet_id, message.messagePayload)
        self.writeHeader(message, len(message.messagePayload))
        message.messageBuffer += message.messagePayload
        try:
            self.socket.send(message.messageBuffer)
        except Exception as e:
            print("Error sending message: " + str(e))


    def receiveMessage(self):
        header = self.socket.recv(7)
        if (len(header) >= 7):
            header = self.readHeader(header)
            packet_id = header[0]
            packet_lenght = header[1]
            packet_version = header[2]
            payload = self.recvall(packet_lenght)
            decryptedPayload = self.cryptoinit.decryptServer(packet_id=packet_id, payload=payload)
            message : PiranhaMessage = LogicSquadMessageFactory.createMessageByType(packet_id, decryptedPayload, self.logicData)
            if message:
                message.decode()
                message.print_message()
                message.execute(self)
                return message
            return None
        

    def readHeader(self, header):
        headerData = []
        headerData.append(int.from_bytes(header[:2], 'big', signed=False))
        headerData.append(int.from_bytes(header[2:5], 'big', signed=False))
        headerData.append(int.from_bytes(header[5:], 'big', signed=False))
        return headerData
    
    def writeHeader(self, message: PiranhaMessage, payloadLen):
        message.messageBuffer += message.getMessageType().to_bytes(2, 'big', signed=False)
        message.messageBuffer += payloadLen.to_bytes(3, 'big', signed=False)
        message.messageBuffer += message.getMessageVersion().to_bytes(2, 'big', signed=False)


    def listen_for_messages(self):
        while self.running:
            time.sleep(0.1)
            try:
                message : PiranhaMessage = self.receiveMessage()
                if message:
                    if message.getMessageType() == LogicSquadPackets.PLAYER_PROFILE_MESSAGE.value:
                        self.returningMessage = message
                        self.stop_signal = True
                    if message.getMessageType() == LogicSquadPackets.LEADERBOARD_DATA_MESSAGE.value:
                        self.leaderboardData = message
                        self.leaderboard_stop_signal = True
                    if message.getMessageType() == LogicSquadPackets.LOCAL_LEADERBOARD_DATA_MESSAGE.value:
                        self.localLeaderboardData = message
                        self.local_leaderboard_stop_signal = True
            except Exception as e:
                print("Error receiving message: " + str(traceback.format_exc()))
                self.running = False
                break

    def stop(self):
        if self.running:
            self.running = False
            self.stop_listener_thread()
            self.stop_sending_keep_alive()
            self.socket.close()
            self.socket = None

    def isPlayerIdValid(self, user_id : str) -> bool:
        pattern = r"^(?:[1-9]?\d)-([1-9]\d{0,8}|214748364[0-7])$"
        return re.match(pattern, user_id)
    
    def send_player_profile(self, user_id : str):
        if self.isPlayerIdValid(user_id):
            current = 0
            self.user_id = user_id
            self.sendMessage(LogicSquadPackets.ASK_PLAYER_PROFILE_MESSAGE.value)
            while not self.stop_signal:
                current += 0.05
                time.sleep(0.05)
                if current >= 0.5:
                    raise TimeoutError()   
            return self.returningMessage.returning_data
        else:
            raise ValueError("Invalid user id")
        
    def ask_player_leaderboard(self):
        current = 0
        self.sendMessage(LogicSquadPackets.ASK_LEADERBOARD_DATA_MESSAGE.value)
        while not self.leaderboard_stop_signal:
            current += 0.05
            time.sleep(0.05)
            if current >= 1.0:
                raise TimeoutError()   
        return self.leaderboardData.returning_data
    
    def ask_player_local_leaderboard(self):
        current = 0
        self.sendMessage(LogicSquadPackets.ASK_LOCAL_LEADERBOARD_DATA_MESSAGE.value)
        while not self.local_leaderboard_stop_signal:
            current += 0.05
            time.sleep(0.05)
            if current >= 1.0:
                raise TimeoutError()   
        return self.localLeaderboardData.returning_data

    def send_keep_alive_message(self):
        self.sendMessage(LogicSquadPackets.KEEP_ALIVE_MESSAGE.value)

    def stop_sending_keep_alive(self):
        self.keep_alive_thread.join()

    def stop_listener_thread(self):
        self.listener_thread.join()

    def activate_send_keep_alive(self):
        while self.running:
            time.sleep(4)
            self.send_keep_alive_message()

    def clear_account(self):
        self.stop_signal = False
        self.leaderboard_stop_signal = False
        self.user_id = ""
        self.returningMessage = None
    


    def stop_listener_thread(self):
        self.listener_thread.join()


