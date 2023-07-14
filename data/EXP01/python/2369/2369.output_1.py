# @lc app=leetcode id=2369 lang=python3
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        
        for i in range(n):
            if self.isValid(nums, i):
                return True
        
        return False
    
    def isValid(self, nums: List[int], start: int) -> bool:
        n = len(nums)
        count = 1
        
        if (start + 1 < n) and (nums[start] == nums[start + 1]):
            return True
        
        if (start + 2 < n) and (nums[start] == nums[start + 1] == nums[start + 2]):
            return True
        
        if (start + 2 < n) and (nums[start] + 1 == nums[start + 1]) and (nums[start + 1] + 1 == nums[start + 2]):
            return True
        
        return False