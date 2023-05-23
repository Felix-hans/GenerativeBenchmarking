# @lc app=leetcode id=1608 lang=python3
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort the array in descending order
        
        n = len(nums)
        for i in range(n):
            if nums[i] < i + 1:
                return -1
            if i == n - 1 or nums[i + 1] < i + 1:
                return i + 1
        return -1