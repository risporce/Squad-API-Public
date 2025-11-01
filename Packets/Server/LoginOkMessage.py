from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets

class LoginOkMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)
        # self.player_high_id : int = None
        # self.player_low_id : int = None
        # #
        # #
        # self.player_pass_token : str = None
        # #
        # #
        # self.major : int = None
        # self.minor: int = None
        # self.build : int = None
        # self.revision : int = None
        # self.env : str = None
        # self.nb_connections : int = None
        # self.minutes_ago_account_creation : int = None
        # self.nb_days_since_account_creation : int = None
        # #
        # self.server_timestamp_at_loginok : str = None
        # self.timestamp_account_creation_date : str = None
        # #
        # #
        # self.country : str = None
        # #
        # self.idk : int # main = 2, little = 1
        # self.event_assets_url : str = None
        # self.game_assets_url : str = None
        # #
        # self.authorisationToken  : str = None



    def encode(self):
        return None
    
    def decode(self):
        #return
        self.player_high_id = self.readInt()
        self.player_low_id = self.readInt()
        self.readInt()
        self.readInt()
        self.player_pass_token = self.readString()
        # self.readString()
        # self.readString()
        # self.major  = self.readInt()
        # self.minor  = self.readInt()
        # self.build  = self.readInt()
        # self.revision  = self.readInt()
        # self.env = self.readString()
        # self.nb_connections = self.readInt()
        # self.minutes_ago_account_creation = self.readInt()
        # self.nb_days_since_account_creation = self.readInt()
        # self.readString()
        # self.server_timestamp_at_loginok = self.readString()
        # self.timestamp_account_creation_date = self.readString()
        # self.readInt()
        # self.readString()
        # self.country = self.readString()
        # self.readString()
        # self.idk = self.readInt()
        # self.event_assets_url = self.readString()
        # self.game_assets_url = self.readString()
        # self.readString()
        # self.authorisationToken = self.readCompressedString()
        # self.readBoolean()
        # self.readBoolean()
        # self.readBoolean()
        # self.readVInt()
        # self.readString()
        # self.readString()
        # self.readString()
        return

    def print_message(self):
        #return
        # print("Start - LoginOkMessage \n")
        # print(f"Player High ID: {self.player_high_id}")
        # print(f"Player Low ID: {self.player_low_id}")
        # print(f"Player Pass Token: {self.player_pass_token}")
        # print(f"Major: {self.major}")
        # print(f"Minor: {self.minor}")
        # print(f"Build: {self.build}")
        # print(f"Revision: {self.revision}")
        # print(f"Env: {self.env}")
        # print(f"Nb Connections: {self.nb_connections}")
        # print(f"Minutes ago account creation: {self.minutes_ago_account_creation}")
        # print(f"Nb days since account creation: {self.nb_days_since_account_creation}")
        # print(f"Server timestamp at loginok: {self.server_timestamp_at_loginok}")
        # print(f"Timestamp account creation date: {self.timestamp_account_creation_date}")
        # print(f"Country: {self.country}")
        # print(f"IDK: {self.idk}")
        # print(f"Event Assets URL: {self.event_assets_url}")
        # print(f"Game Assets URL: {self.game_assets_url}")
        # print(f"AuthorisationToken: {self.authorisationToken}")
        # print("End - LoginOkMessage \n")
        return

    def getMessageType(self):
        return LogicSquadPackets.LOGIN_OK_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        #client.sendMessage(LogicSquadPackets.ASK_PLAYER_PROFILE_MESSAGE.value)
        return