from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets
import json
from ClientGlobals import Configs

class LoginFailedMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)
        self.error_code : int
        self.fingerprint : bytes



    def encode(self):
        return None
    
    def decode(self):
        self.error_code = self.readInt()
        self.readString()
        self.readString()
        self.readString()
        self.readString()
        self.readString()
        self.readInt()
        self.readBoolean()
        self.fingerprint = self.readCompressedString()
    
    def print_message(self):
        return

    def getMessageType(self):
        return LogicSquadPackets.LOGIN_FAILED_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        if self.error_code == 7:
            fingerprint_str : str = self.fingerprint.decode('utf-8')
            data = json.loads(fingerprint_str)
            sha: str = data["sha"]
            version : str = data["version"]
            version_split = version.split(".")
            print(version_split)
            config = Configs()
            config.global_data.client_hello_message.major = int(version_split[0])
            config.global_data.login_message.client_major = int(version_split[0])

            config.global_data.client_hello_message.build = int(version_split[1])
            config.global_data.login_message.client_build = int(version_split[1])

            config.global_data.client_hello_message.minor = int(version_split[2])
            config.global_data.login_message.client_minor = int(version_split[2])

            config.global_data.client_hello_message.content_hash = sha
            config.global_data.login_message.resource_sha = sha
            
            config.save_configuration()
            #config.set(sha, "LoginMessage", "ResourceSha")
            #config.set(sha, "ClientHelloMessage", "ContentHash")
            print(f"[INFO] game updated to {version} with new sha {sha}")
        return