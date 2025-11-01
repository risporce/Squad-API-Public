from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets

class ServerHelloMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)
        self.session_key = None
        self.bytes_length = None

    def encode(self):
        return None
    
    def decode(self):
        self.bytes_length = self.readInt()
        self.session_key = self.readBytes(self.bytes_length)
        return None
    
    def print_message(self):
        # print("Start - ServerHelloMessage \n")
        # print("SessionKey: " + str(self.session_key.hex()))
        # print("End - ServerHelloMessage \n")
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.SERVER_HELLO_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        client.sendMessage(LogicSquadPackets.LOGIN_MESSAGE.value)