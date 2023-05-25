''' 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
from typing import List

# My solution: O(n^2)
nums = [1,2,3,2,2]
target = 4

# out = Solution()
# out.twoSum(nums, target)
# for i in range(len(nums)):
#     for j in range(1, len(nums)):
#         if i == j:
#             pass
#         elif nums[i] + nums[j] == target:
#             print([i, j])


# Fastest solution: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_table:
                return [hash_table[complement], i]
            hash_table[num] = i