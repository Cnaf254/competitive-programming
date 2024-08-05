def findMaxConsecutiveOnes(nums: List[int]) -> int:
    return max(map(len, ''.join(map(str, nums)).split('0')))
