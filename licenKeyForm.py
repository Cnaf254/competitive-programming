def licenseKeyFormatting(s: str, k: int) -> str:
    s = s.replace('-', '').upper()
    size = len(s)
    first = size % k
    parts = [s[:first]] if first else []
    for i in range(first, size, k):
        parts.append(s[i:i + k])
    return '-'.join(parts)
