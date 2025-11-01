from Packets.PiranhaMessage import PiranhaMessage
from ClientGlobals import Configs
from Packets.PacketsEnum import LogicSquadPackets

class LoginMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)

    def encode(self, fields):
        config = Configs()
        self.writeInt(fields["h"])
        self.writeInt(fields["l"])
        self.writeString(fields["p"])
        self.writeInt(config.global_data.login_message.client_major)
        self.writeInt(config.global_data.login_message.client_build)
        self.writeInt(config.global_data.login_message.client_minor)
        self.writeString(config.global_data.login_message.resource_sha)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.device)
        self.writeInt(config.global_data.login_message.int_default) # locales.csv high id
        self.writeInt(config.global_data.login_message.locales_csv_id)
        self.writeString(config.global_data.login_message.prefered_device_language)
        self.writeString(str(config.global_data.login_message.imei))
        self.writeString(config.global_data.login_message.os_version)
        self.writeBoolean(config.global_data.login_message.is_android)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeBoolean(config.global_data.login_message.is_advertising_enabled)
        self.writeString(config.global_data.login_message.apple_ifv)
        self.writeInt(config.global_data.login_message.rnd_key)
        self.writeVInt(config.global_data.login_message.app_store)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.client_version)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeVInt(config.global_data.login_message.int_default)
        self.writeString(config.global_data.login_message.device_name)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeString(config.global_data.login_message.string_default)
        self.writeBoolean(config.global_data.login_message.boolean_default)
        self.writeBoolean(config.global_data.login_message.boolean_default)
        self.writeCompressedString(config.global_data.login_message.supercell_id_token)
        self.writeVInt(config.global_data.login_message.int_default)
        self.writeBoolean(config.global_data.login_message.boolean_default)
    
    def decode(self):
        return None
    
    def print_message(self):
        return None
    
    def getMessageType(self):
        return LogicSquadPackets.LOGIN_MESSAGE.value
    
    def getMessageVersion(self):
        return 10
    
    def execute(self):
        return