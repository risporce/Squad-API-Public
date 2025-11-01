from Files.LogicData.LogicData import LogicData
import csv
class LogicSkinsData(LogicData):
    csv_id = 55
    def __init__(self):
        super().__init__()
        self.data_reference = {}


    def createReferences(self):
        with open('Files/Assets/skins.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            next(csv_reader)
            line_count = 0

            for row in csv_reader:
                if row['Name']:
                    key = line_count
                    self.data_reference[key] = {
                        'Name':row['Name'],
                        'Rarity':int(row['Rarity']) if row.get('Rarity') else None,
                    }
                    line_count +=1

        return self