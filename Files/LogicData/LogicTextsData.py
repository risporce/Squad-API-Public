from Files.LogicData.LogicData import LogicData
import csv
class LogicTextsData(LogicData):
    csv_id = 0
    def __init__(self):
        super().__init__()
        self.data_reference = {}


    def createReferences(self):
        with open('Files/Assets/texts.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            next(csv_reader)
            line_count = 0

            for row in csv_reader:
                if row['TID']:
                    key = row['TID']
                    self.data_reference[key] = {
                        'Text':row['EN'],
                    }
                    line_count +=1
        return self