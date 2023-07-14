# @lc app=leetcode id=2420 lang=python3
from typing import List

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        
        for i in range(k, n - k):
            if self.isGoodIndex(nums, i, k):
                result.append(i)
                
        return result
    
    def isGoodIndex(self, nums: List[int], idx: int, k: int) -> bool:
        for i in range(k):
            if nums[idx - i] < nums[idx - i - 1] or nums[idx + i] > nums[idx + i + 1]:
                return False
        return True