# @lc app=leetcode id=413 lang=python3
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0  # Total count of arithmetic subarrays
        current = 0  # Count of arithmetic subarrays ending at current index
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                count += current
            else:
                current = 0
        
        return count