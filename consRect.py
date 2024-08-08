def constructRectangle(area: int) -> List[int]:
    for w in range(int(area**0.5), 0, -1):
        if area % w == 0:
            return [area // w, w]
