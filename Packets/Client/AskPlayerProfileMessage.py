from Packets.PiranhaMessage import PiranhaMessage
from ClientGlobals import Configs
from Packets.PacketsEnum import LogicSquadPackets
class AskPlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self, fields : dict):
        config = Configs()
        self.writeInt(fields["high"])
        self.writeInt(fields["low"])
        self.writeBoolean(True)

    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.ASK_PLAYER_PROFILE_MESSAGE.value
    
    def getMessageVersion(self):
        return 10
    
    def execute(self):
        return