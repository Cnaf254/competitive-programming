def findComplement(num: int) -> int:
    mask = (1 << num.bit_length()) - 1
    return num ^ mask
