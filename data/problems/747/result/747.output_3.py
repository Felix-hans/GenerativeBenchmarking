# @lc app=leetcode id=747 lang=python3
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)
        
        for num in nums:
            if num != largest and num * 2 > largest:
                return -1
        
        return index