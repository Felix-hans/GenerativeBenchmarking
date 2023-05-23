# @lc app=leetcode id=1608 lang=python3
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        
        for i in range(n):
            if nums[i] >= n - i:
                if i == 0 or nums[i-1] < n - i:  # Check if the condition is satisfied
                    return n - i
        
        return -1  # Return -1 if no special number is found