

def level_to_world(worldID: int, squadLeagueId: int) -> str:
    if (worldID <= 14):
        return "Green World"
    elif (worldID <= 34):
        return "Desert World"
    elif (worldID <= 59):
        return "Royal World"
    elif (worldID <= 89):
        return "Beach World"
    elif (worldID <= 119):
        return "Ice World"
    elif (worldID <= 149):
        return "Lava World"
    elif (worldID < 179):
        return "Spooky World"
    if (worldID == 179 and squadLeagueId is not None):
        return "Treasure Room"
    elif (worldID == 179 and squadLeagueId is None):
        return "Spooky World"