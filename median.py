def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the smaller array to minimize the binary search range
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    imin, imax = 0, m
    half_len = (m + n + 1) // 2

    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i

        if i < m and nums1[i] < nums2[j - 1]:
            # i is too small, move right
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            # i is too large, move left
            imax = i - 1
        else:
            # i is perfect
            max_of_left = 0
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left  # Odd case

            min_of_right = 0
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2
