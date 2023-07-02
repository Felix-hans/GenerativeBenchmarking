# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        seen = {}  # Store the indices and values encountered so far
        
        for i in range(n):
            for value in range(nums[i] - valueDiff, nums[i] + valueDiff + 1):
                if value in seen and abs(seen[value] - i) <= indexDiff:
                    return True
            
            seen[nums[i]] = i  # Store the current index for the current value
            
            if i >= indexDiff:
                del seen[nums[i - indexDiff]]
        
        return False