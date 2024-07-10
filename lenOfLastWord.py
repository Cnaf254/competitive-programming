def lengthOfLastWord(s: str) -> int:
    return len(s.rstrip().split()[-1])
