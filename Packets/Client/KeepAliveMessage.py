from Packets.PiranhaMessage import PiranhaMessage
from ClientGlobals import Configs
from Packets.PacketsEnum import LogicSquadPackets

class KeepAliveMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self, fields):
        return
    
    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.KEEP_ALIVE_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self):
        return