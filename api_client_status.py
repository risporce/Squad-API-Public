import socket
from LogicSquadMessageFactory import LogicSquadMessageFactory
from Crypto import Crypto
import threading
import queue
from Packets.PiranhaMessage import PiranhaMessage
import time
import traceback
from Packets.Server.PlayerProfileMessage import PlayerProfileMessage
import re
from Packets.PacketsEnum import LogicSquadPackets
import asyncio
from ClientGlobals import Configs


class APIClientStatus:
    def __init__(self, configs: Configs, account: dict):
        self.host = configs.global_data.server.server
        self.port = configs.global_data.server.port
        self.socket = None
        self.cryptoinit = Crypto(configs.global_data.server.server_public_key)
        self.packet_queue = queue.Queue()
        self.running = False
        self.stop_signal = False
        self.last_status_code: int = None
        self.listener_thread = None
        self.account = account

    def recvall(self, lenght: int) -> bytes:
        data = b''
        while len(data) < lenght:
            s = self.socket.recv(lenght)
            data += s
        return data

    def connect(self):
        current = 0
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        self.running = True
        self.sendMessage(LogicSquadPackets.CLIENT_HELLO_MESSAGE.value)
        self.listener_thread = threading.Thread(target = self.listen_for_messages)
        self.listener_thread.start()
        while not self.stop_signal:
            current += 0.05
            time.sleep(0.05)
            if current >= 1.5:
                raise TimeoutError()
        self.stop()
        return self.last_status_code



    def sendMessage(self, packet_id):
        fields = {}
        if packet_id == LogicSquadPackets.LOGIN_MESSAGE.value:
            fields["h"] = self.account.get("h")
            fields["l"] = self.account.get("l")
            fields["p"] = self.account.get("p")
        message: PiranhaMessage = LogicSquadMessageFactory.createMessageByType(packet_id, b'', None)
        fields["Status"] = True
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
            message : PiranhaMessage = LogicSquadMessageFactory.createMessageByType(packet_id, decryptedPayload, None)

            if message:
                if packet_id == LogicSquadPackets.LOGIN_OK_MESSAGE.value:
                    self.last_status_code = 0
                    return message
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
                    if message.getMessageType() == LogicSquadPackets.LOGIN_OK_MESSAGE.value or message.getMessageType() == LogicSquadPackets.LOGIN_FAILED_MESSAGE.value:
                        if message.getMessageType() == LogicSquadPackets.LOGIN_FAILED_MESSAGE.value:
                            self.last_status_code = message.error_code
                        self.stop_signal = True
                        break
            except Exception as e:
                print("Error receiving message: " + str(traceback.format_exc()))
                self.running = False
                break

    def stop(self):
        if self.running:
            self.running = False
            self.listener_thread.join()
            self.socket.close()
            self.socket = None

    

