def findRelativeRanks(score: List[int]) -> List[str]:
    sorted_scores = sorted(score, reverse=True)
    rank = {v: str(i + 1) if i > 2 else ["Gold Medal", "Silver Medal", "Bronze Medal"][i]
            for i, v in enumerate(sorted_scores)}
    return [rank[s] for s in score]
