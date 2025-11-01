from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets
import json
from ClientGlobals import Configs

class KeepAliveServerMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)



    def encode(self):
        return None
    
    def decode(self):
        return
    
    def print_message(self):
        return

    def getMessageType(self):
        return LogicSquadPackets.KEEP_ALIVE_SERVER_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        return