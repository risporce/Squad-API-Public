from Packets.PiranhaMessage import PiranhaMessage
from ClientGlobals import Configs
from Packets.PacketsEnum import LogicSquadPackets

class ClientHelloMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self, fields):
        config = Configs()
        self.writeInt(config.global_data.client_hello_message.protocol)
        self.writeInt(config.global_data.client_hello_message.key_version)
        self.writeInt(config.global_data.client_hello_message.major)
        self.writeInt(config.global_data.client_hello_message.build)
        self.writeInt(config.global_data.client_hello_message.minor)
        self.writeString(config.global_data.client_hello_message.content_hash)
        self.writeInt(config.global_data.client_hello_message.device_type)
        self.writeInt(config.global_data.client_hello_message.app_store)
        return
    
    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.CLIENT_HELLO_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self):
        return