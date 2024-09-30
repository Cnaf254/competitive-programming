def findLUSlength(a: str, b: str) -> int:
    return max(len(a), len(b)) if a != b else -1
