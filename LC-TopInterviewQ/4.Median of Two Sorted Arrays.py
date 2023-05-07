'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
'''

# My Solution: O((m+n) log(m+n))
from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    my_list = sorted(nums1+nums2)
    mid = len(my_list) // 2
    res = (my_list[mid] + my_list[~mid]) / 2
    return res
    

# Fastest solution (Binary search): O(log(m+n))

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m, n = len(nums1), len(nums2)
    if m > n:
        nums1, nums2, m, n = nums2, nums1, n, m
    imin, imax, half_len = 0, m, (m + n + 1) // 2
    while imin <= imax:
        i = (imin + imax) // 2
        j = half_len - i
        if i < m and nums2[j-1] > nums1[i]:
            # i is too small, increase it
            imin = i + 1
        elif i > 0 and nums1[i-1] > nums2[j]:
            # i is too big, decrease it
            imax = i - 1
        else:
            # i is perfect
            if i == 0:
                max_of_left = nums2[j-1]
            elif j == 0:
                max_of_left = nums1[i-1]
            else:
                max_of_left = max(nums1[i-1], nums2[j-1])
            if (m + n) % 2 == 1:
                return max_of_left
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right) / 2


print(findMedianSortedArrays(nums1=[1,2,3], nums2=[1,2]))