def detectCapitalUse(word: str) -> bool:
    return word.isupper() or word.islower() or word.istitle()
