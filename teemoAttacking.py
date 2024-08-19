def findPoisonedDuration(timeSeries: List[int], duration: int) -> int:
    total_time = 0
    for i in range(len(timeSeries) - 1):
        total_time += min(timeSeries[i + 1] - timeSeries[i], duration)
    return total_time + duration
