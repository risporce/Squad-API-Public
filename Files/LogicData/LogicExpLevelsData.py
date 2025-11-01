from Files.LogicData.LogicData import LogicData
import csv
class LogicExpLevelData(LogicData):
    csv_id = 54
    def __init__(self):
        super().__init__()
        self.data_reference = {}
        self.weight = 0


    def createReferences(self):
        with open('Files/Assets/exp_levels.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            next(csv_reader)
            line_count = 0

            for row in csv_reader:
                if row['Name']:
                    exp = int(row['ExpToNextLevel'])
                    key = line_count
                    self.data_reference[key] = {
                        'Name':row['Name'],
                        'ExpToNextLevel':int(row['ExpToNextLevel']),
                    }
                    self.weight += exp
                    line_count +=1
        return self