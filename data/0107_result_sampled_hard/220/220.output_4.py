# @lc app=leetcode id=220 lang=python3
from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        sorted_set = []
        
        for i in range(n):
            if i > indexDiff:
                sorted_set.remove(nums[i - indexDiff - 1])
            
            left = 0
            right = len(sorted_set) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if abs(sorted_set[mid] - nums[i]) <= valueDiff:
                    return True
                elif sorted_set[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            sorted_set.insert(left, nums[i])
        
        return False