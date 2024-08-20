def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    stack, greater = [], {}
    for num in nums2:
        while stack and stack[-1] < num:
            greater[stack.pop()] = num
        stack.append(num)
    return [greater.get(num, -1) for num in nums1]
