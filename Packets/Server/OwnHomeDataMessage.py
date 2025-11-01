from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets

class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self):
        return None
    
    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.OWN_HOME_DATA_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        return