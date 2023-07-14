# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        num_set = set()  # Set to store the unique values within the specified index difference
        
        for i in range(n):
            if i > indexDiff:
                num_set.remove(nums[i - indexDiff - 1])
            
            for num in num_set:
                if abs(num - nums[i]) <= valueDiff:
                    return True
            
            num_set.add(nums[i])
        
        return False