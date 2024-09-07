def convertToBase7(num: int) -> str:
    if num == 0: return "0"
    sign = "-" if num < 0 else ""
    num = abs(num)
    res = ""
    while num:
        res = str(num % 7) + res
        num //= 7
    return sign + res
