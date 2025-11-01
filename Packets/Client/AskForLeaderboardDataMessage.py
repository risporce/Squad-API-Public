from Packets.PiranhaMessage import PiranhaMessage
from ClientGlobals import Configs
from Packets.PacketsEnum import LogicSquadPackets

class AskForLeaderboardDataMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self, fields : dict):
        config = Configs()
        #self.writeInt(fields["high"])
        #self.writeInt(fields["low"])
        a = False
        self.writeBoolean(a)
        # if a:
        #     self.writeInt(4001)
        #     self.writeInt(1)
        

    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.ASK_LEADERBOARD_DATA_MESSAGE.value
    
    
    def getMessageVersion(self):
        return 0
    
    def execute(self):
        return