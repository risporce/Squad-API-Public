

def extract_ids(globalId : int) -> list[int, int]:
    high = globalId // 100000
    low = globalId % 100000
    return [high, low]

def write_global_id(high: int, low : int) -> int:
    return high * 100000 + low

