from Packets.PiranhaMessage import PiranhaMessage
from Packets.PacketsEnum import LogicSquadPackets
from Utils.LevelToWorld import level_to_world
from Utils.SupercellGlobalIds import extract_ids, write_global_id
import json

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData, logicData):
        super().__init__(messageData, logicData)
        self.json_data : str
        self.player_high_id : int
        self.player_low_id : int
        self.some_high_id : int
        self.some_low_id : int
        self.has_this_value : bool
        self.long_weird_value_high : int
        self.long_weird_value_low : int
        self.player_name : str
        self.game_center_id : int
        #
        self.experience_level : int
        self.experience_gained : int
        #
        #
        #
        #
        self.squad_league_trophies : int
        self.current_world : int
        self.squad_league_level : int
        self.a : int
        self.nbSquadLeagueGames : int
        self.region : int
        self.new_str_reference : str # v12
        self.commodity_count : int

        self.returning_data : dict = dict()
        self.resources : dict = {}
        self.avatar_stats : dict = {}
        self.variables : dict = {}
        self.other_profile_information : dict = {}

        self.v13_long_high : int
        self.v13_long_low : int
        self.v13_int : bool
        self.v13_vint : int

        # after that it's commodify


    def encode(self):
        return None
    
    def decode(self):
        # print(self.messageBuffer.hex())
        #LogicClientAvatar
        self.json_data = self.readCompressedString().decode('utf-8')
        #print(self.json_data)
        self.player_high_id = self.readInt()
        self.player_low_id = self.readInt()
        self.some_high_id = self.readInt()
        self.sone_low_id = self.readInt()
        self.has_this_value = self.readBoolean()
        self.long_weird_value_high  = self.readInt()
        self.long_weird_value_low  = self.readInt()
        self.player_name  = self.readString()
        self.readVInt()
        self.readBoolean() # True
        self.readInt() #high_id of gamecenter
        self.game_center_id = self.readInt()
        self.experience_level = self.readVInt()
        self.experience_gained = self.readVInt()
        self.readString()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.squad_league_trophies = self.readVInt()
        self.current_world = self.readVInt()
        self.squad_league_level = self.readVInt()
        self.a = self.readInt()
        self.nbSquadLeagueGames = self.readInt()
        self.value4006_enabled = self.readBoolean()
        if self.value4006_enabled:
            self.readInt()
            self.region = self.readInt()
        self.readInt()
        self.new_str_reference = self.readString() # v12
        #print(self.getByteArray().hex())
        #print(self.new_str_reference)
        #print(self.readVInt())
        self.v13_long_high = self.readInt()
        #print(self.v13_long_high)
        self.v13_long_low = self.readInt()
        #print(self.v13_long_low)
        self.v13_int = self.readInt()
        #print(self.v13_int)
        self.v13_vint = self.readVInt()
        #print(self.v13_vint)
        self.commodity_count = self.readVInt()
        #print(self.commodity_count)


#for x in range(commodityCount):
        # start commodity count section
        count = self.readVInt() # unlocked resource
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            resource_id = self.readVLong()
            if (self.readBoolean()): # resource gained
                resource_value = self.readVInt()
            else:
                resource_value = None
            self.resources[resource_id] = resource_value

        count = self.readVInt() # unlocked avatar stats
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            avatar_stat_id =  self.readVLong() # avatar stat id
            if (self.readBoolean()): # avatar stat  gained
                avaytar_stat_value = self.readVInt() # avatar stat  amount
            else:
                avaytar_stat_value = None
            self.avatar_stats[avatar_stat_id] = avaytar_stat_value

        count = self.readVInt() # unlocked variables
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            variable_id =  self.readVLong() # variable id
            if (self.readBoolean()): # variable gained
                variable_value = self.readVInt() # variable amount
            else:
                variable_value = None
            self.variables[variable_id] = variable_value

        count = self.readVInt()
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            self.readVLong()
            if (self.readBoolean()):
                self.readVInt()

        count = self.readVInt() #unk for now
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            self.readVLong()
            if (self.readBoolean()):
                self.readVInt()

        count = self.readVInt() # unk for now
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            self.readVLong()
            if (self.readBoolean()):
                self.readVInt()

        count = self.readVInt()
        for y in range(count):
            if self.readBoolean():
                self.readVInt()
            self.readVLong()
            if (self.readBoolean()):
                self.readVInt()
        #nd commodity count section


    def print_message(self):
        decoded_json_str : dict = json.loads(self.json_data)
        index = 0
        for character in decoded_json_str["chars"]["c"]:
            high_and_low : list[int, int] = extract_ids(int(character['data']))
            csv_row : dict = self.logicData.get_data(high_and_low[0], high_and_low[1])
            character_real_name = csv_row.get('TID')
            text_csv_row : dict = self.logicData.get_data(0, -1, character_real_name)
            character_name = text_csv_row.get("Text")
            if len(character.get('selLineup', [])) > 0:
                lineup_chars_array = character.get("selLineup", [])


                character_lineup = []
                for lineup_char in lineup_chars_array:
                    c_index = 0
                    c_real_name = ""
                    c_character_level = 1
                    for player_character in decoded_json_str["chars"]["c"]:
                        #print(player_character)
                        if (int(player_character['data']) == lineup_char and int(player_character["data"] != int(character["data"]))):
                            character_high_and_low: list[int, int] = extract_ids(int(player_character["data"]))
                            character_csv_row : dict = self.logicData.get_data(character_high_and_low[0], character_high_and_low[1])
                            c_tid_name = character_csv_row.get('TID')
                            c_text_csv_row : dict = self.logicData.get_data(0, -1, c_tid_name)
                            c_real_name = c_text_csv_row.get('Text')
                            c_character_level = int(player_character.get("lvl", 0))
                            break
                    if c_real_name != "":
                        character_lineup.append({"Name": c_real_name, "Lvl": c_character_level, "CharacterId": lineup_char})
                    c_index += 1
                decoded_json_str["chars"]["c"][index]["LineupCharacters"] = character_lineup # fix the overwrite
                #decoded_json_str["chars"]["c"][index]["LineupCharacters"]["Lvl"] = 
                #decoded_json_str["chars"]["c"][index]["LineupCharacters"]["Name"] = c_real_name


            if len(character.get("selPowers", [])) > 0:
                power_lineup = []
                lineup_powers = character.get("selPowers", [])
                for power in lineup_powers:
                    c_index = 0
                    c_real_name = ""
                    c_power_level = 1
                    for player_character in decoded_json_str["chars"]["c"]:
                        if (int(player_character['data']) == power and int(player_character["data"] != int(character["data"]))):
                            character_high_and_low: list[int, int] = extract_ids(int(player_character["data"]))
                            character_csv_row : dict = self.logicData.get_data(character_high_and_low[0], character_high_and_low[1])
                            c_tid_name = character_csv_row.get('TID')
                            c_text_csv_row : dict = self.logicData.get_data(0, -1, c_tid_name)
                            c_real_name = c_text_csv_row.get('Text')
                            #print(player_character)
                            c_power_level = self.get_power_level_from_character_level(int(player_character.get("lvl", 0)))
                            break
                    if c_real_name != "":
                        power_lineup.append({"Name": c_real_name, "Lvl": c_power_level, "CharacterId": power})
                    c_index += 1
                decoded_json_str["chars"]["c"][index]["LineupPowers"] = power_lineup
                            #decoded_json_str["chars"]["c"][index]["LineupCharacters"]["Lvl"] = self.get_power_level_from_character_level(player_character["materialC"])
                            #decoded_json_str["chars"]["c"][index]["LineupPowers"]["Name"] = c_real_name



            decoded_json_str["chars"]["c"][index]['Name'] = csv_row.get('Name')
            decoded_json_str["chars"]["c"][index]["RealName"] = character_name
            decoded_json_str["chars"]["c"][index]['Rarity'] = csv_row.get('Rarity')
            decoded_json_str["chars"]["c"][index]['FormationRole'] = csv_row.get('FormationRole')
            decoded_json_str["chars"]["c"][index]['IP'] = csv_row.get('IP')
            decoded_json_str["chars"]["c"][index]['Position'] = csv_row.get('Position')
            decoded_json_str["chars"]["c"][index]['Class'] = csv_row.get('Class')
            decoded_json_str["chars"]["c"][index]['Type'] = csv_row.get('Type')
            #print(csv_row)
            index += 1
            #print(character)
        decoded_json_str["resources"] = []
        for resource_id, resource_value in self.resources.items():
            high_and_low = extract_ids(resource_id)
            csv_row  = self.logicData.get_data(high_and_low[0], high_and_low[1])
            resource_data = {
            "name": csv_row.get('Name'),
            "value": resource_value
            }
            decoded_json_str["resources"].append(resource_data)

        decoded_json_str["avatar_stats"] = []
        for avatar_stat_id, avatar_stat_value in self.avatar_stats.items():
            high_and_low = extract_ids(avatar_stat_id)
            csv_row = self.logicData.get_data(high_and_low[0], high_and_low[1])
            decoded_json_str["avatar_stats"].append({
             "name": csv_row.get('Name'), 
             "value": avatar_stat_value
            })
        decoded_json_str["variables"] = []
        for variable_id, variable_value in self.variables.items():
            high_and_low = extract_ids(variable_id)
            csv_row = self.logicData.get_data(high_and_low[0], high_and_low[1])
            decoded_json_str["variables"].append({
             "name": csv_row.get('Name'), 
             "value": variable_value
            })

        current_world_str = level_to_world(self.current_world, self.squad_league_level)
        region_high_and_low : list[int, int] = extract_ids(self.region)
        region_data = self.logicData.get_data(region_high_and_low[0], region_high_and_low[1])
        decoded_json_str["other"] = []
        decoded_json_str["other"].append({"name": "exp", "value": self.experience_level})
        decoded_json_str["other"].append({"name": "expGained", "value": self.experience_gained})
        decoded_json_str["other"].append({"name": "SQTrophies", "value": self.squad_league_trophies})
        decoded_json_str["other"].append({"name": "SQLevel", "value": self.squad_league_level})
        decoded_json_str["other"].append({"name": "currentWorld", "value": current_world_str})
        decoded_json_str["other"].append({"name": "squadLevel", "value": self.current_world})
        decoded_json_str["other"].append({"name": "a", "value": self.a})
        decoded_json_str["other"].append({"name": "nbSquadLeagueGames", "value": self.nbSquadLeagueGames})
        decoded_json_str["other"].append({"name": "new_v12", "value": self.new_str_reference})
        decoded_json_str["other"].append({"name": "new_v13_long_high", "value": self.v13_long_high})
        decoded_json_str["other"].append({"name": "new_v13_long_low", "value": self.v13_long_low})
        decoded_json_str["other"].append({"name": "new_v13_int", "value": self.v13_int})
        decoded_json_str["other"].append({"name": "new_v13_vint", "value": self.v13_vint})
        #print(decoded_json_str["chars"]["c"][0])

        encoded_json_str = json.dumps(decoded_json_str)
        self.returning_data["jsonStr"] = encoded_json_str
        self.returning_data["playerName"] = self.player_name
        self.returning_data["regionName"] = region_data["DisplayName"]
        self.returning_data["regionCode"] = region_data["Name"]
        #print(self.returning_data, flush=True)
        #print(self.json_data)
    
    def getMessageType(self):
        return LogicSquadPackets.PLAYER_PROFILE_MESSAGE.value
    
    def getMessageVersion(self):
        return 0
    
    def execute(self, client):
        return
    
    # def get_character_level(self, character_materials: list[int]):
    #     for i in reversed(range(len(character_materials))):
    #         if character_materials[i -1] != 0:
    #             return i
            
    def get_power_level_from_character_level(self, lvl: int):
        #character_level = self.get_character_level(character_materials)
        return 2 if lvl >= 4 else 1