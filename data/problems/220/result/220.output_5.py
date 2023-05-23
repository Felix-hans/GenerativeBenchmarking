# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        if n <= 1:
            return False
        
        window = {}  # Sliding window of size indexDiff
        
        for i in range(n):
            for j in range(max(0, i - indexDiff), i):
                if abs(nums[i] - window[j]) <= valueDiff:
                    return True
            
            window[i] = nums[i]
            
            if i >= indexDiff:
                del window[i - indexDiff]
        
        return False