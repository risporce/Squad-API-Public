from abc import ABC, abstractmethod

class LogicData(ABC):
    def __init__(self):
        self.data_reference = {}

    def createReferences(self):
        for subclass in LogicData.__subclasses__():
            instance = subclass().createReferences()
            self.data_reference[instance.csv_id] = instance.data_reference

    def get_data(self, csv_index : int, row_id : int, row_name_index: str = ""):
        data = self.data_reference.get(csv_index)
        if data:
            if row_id != -1:
                return data.get(row_id)
            if (row_name_index != ""):
                return data.get(row_name_index)
        else:
            return None

    
