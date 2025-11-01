from Files.LogicData.LogicData import LogicData
import csv
class LogicCharacterData(LogicData):
    csv_id = 8
    def __init__(self):
        super().__init__()
        self.data_reference = {}


    def createReferences(self):
        with open('Files/Assets/characters.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=',')
            next(csv_reader)
            line_count = 0

            for row in csv_reader:
                if row['Name']:
                    if row['Type'] == 'Player' or row["Type"] == 'PlayerHero':
                        key = line_count
                        self.data_reference[key] = {
                            'Name':row.get('Name'),
                            'TID': row.get('TID'),
                            'Rarity':int(row['Rarity']) if row.get('Rarity') else None,
                            'FormationRole':row.get('FormationRole', None),
                            'Position': row.get('Position', None),
                            'Class': row.get('Class', None),
                            'ClassHealthPoint': int(row['ClassHealthPoints']) if row.get('ClassHealthPoints') else None,
                            'ClassAttackPoint': int(row['ClassAttackPoints']) if row.get('ClassAttackPoints') else None,
                            'IP': row.get('IP', None),
                            'Type': row.get("Type", "")
                        }
                    line_count +=1
        return self