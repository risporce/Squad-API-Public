from Files.LogicData.LogicData import LogicData
import csv
class LogicSpellsData(LogicData):
    csv_id = 27
    def __init__(self):
        super().__init__()
        self.data_reference = {}
        self.total_weight = 0


    def createReferences(self):
        with open('Files/Assets/spells.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            next(csv_reader)
            line_count = 0

            for row in csv_reader:
                if row['Name']:
                    weight = int(row['Weight']) if row.get('Weight') else None
                    key = line_count
                    self.data_reference[key] = {
                        'Name':row.get('Name'),
                        'Weight': weight,
                    }
                    if weight:
                        self.total_weight += weight
                    line_count +=1
        return self