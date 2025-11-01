from Utils.Parser.ByteStream import ByteStream
from Files.LogicData import LogicData

class PiranhaMessage(ByteStream):
    def __init__(self, messageData, logicData : LogicData):
        super().__init__(messageData)
        self.messageBuffer = messageData
        self.logicData : LogicData = logicData
        self.fields = {}

    def encode(self, fields : dict):
        raise NotImplementedError("Subclasses must implement encode")
    
    def decode(self):
        raise NotImplementedError("Subclasses must implement decode")
    
    def print_message(self):
        raise NotImplementedError("Subclasses must implement printing")
    
    def getMessageType(self):
        raise NotImplementedError("Subclasses must implement getting message type")
    
    def getMessageVersion(self):
        raise NotImplementedError("Subclasses must implement getting message version")
    
    def execute(self, apiClient):
        raise NotImplementedError("Subclasses must implement execution")

    