def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    while m > 0 and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[m+n-1] = nums1[m-1]
            m -= 1
        else:
            nums1[m+n-1] = nums2[n-1]
            n -= 1
    nums1[:n] = nums2[:n]
