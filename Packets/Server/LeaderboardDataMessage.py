from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets
from Utils.LevelToWorld import level_to_world
from Utils.SupercellGlobalIds import extract_ids, write_global_id
import json


class LeaderboardPlayerData():
    def __init__(self):
        self.player_high_id : int
        self.player_low_id : int
        self.player_name : str
        self.trophies : int
        self.position : int
        self.country : str

class LeaderboardDataMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)
        self.leaderboard_count : int
        self.leaderboard_player_list : list[LeaderboardPlayerData] = []
        self.returning_data = {}




    def encode(self):
        return None
    
    def decode(self):
        #print(self.messageBuffer.hex())
        self.leaderboard_count = self.readVInt()
        for i in range(self.leaderboard_count):
            player = LeaderboardPlayerData()
        # before object decode
            if self.readBoolean():
                self.readVInt()
        # object
            if self.readBoolean():
                player.player_high_id = self.readInt()
                player.player_low_id = self.readInt()
            if self.readBoolean():
                player.player_name = self.readString()
            
            if self.readBoolean():
                player.trophies = self.readVInt()

            if self.readBoolean():
                player.position = self.readVInt()

            if self.readBoolean(): # related to positioning too, maybe best position or previous position
                self.readVInt()

            if self.readBoolean(): # el
                self.readVInt()

            if self.readBoolean(): # aw
                self.readVInt()

            if self.readBoolean(): # al
                self.readVInt()

            if self.readBoolean(): # ws
                self.readVInt()

            if self.readBoolean(): #l
                self.readVInt()

            if self.readBoolean(): 
                player.country = self.readString()

            if self.readBoolean(): #aId
                self.readLong()# alliance id, always false since no alliance yet, and there's other data, ohd_88 for name and ohd_240 for badge

            if self.readBoolean(): #sid
                self.readVInt()

            self.leaderboard_player_list.append(player)
        self.readInt()


    def print_message(self):
        for i in range(self.leaderboard_count):
            self.returning_data[self.leaderboard_player_list[i].position] = {"ID": str(self.leaderboard_player_list[i].player_high_id) + "-" + str(self.leaderboard_player_list[i].player_low_id),
                                                                             "Name": getattr(self.leaderboard_player_list[i], "player_name", ""),
                                                                             "Trophies": self.leaderboard_player_list[i].trophies,
                                                                             "Position": self.leaderboard_player_list[i].position,
                                                                             "Country": getattr(self.leaderboard_player_list[i], "country", "")}
    
    def getMessageType(self):
        return LogicSquadPackets.LEADERBOARD_DATA_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        return