# @lc app=leetcode id=220 lang=python3
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        n = len(nums)
        if n <= 1 or indexDiff <= 0:
            return False
        
        num_dict = {}
        for i in range(n):
            num = nums[i]
            bucket = num // (valueDiff + 1)
            
            if bucket in num_dict:
                return True
            
            if bucket - 1 in num_dict and abs(num - num_dict[bucket - 1]) <= valueDiff:
                return True
            
            if bucket + 1 in num_dict and abs(num - num_dict[bucket + 1]) <= valueDiff:
                return True
            
            num_dict[bucket] = num
            
            if i >= indexDiff:
                num_dict.pop(nums[i - indexDiff] // (valueDiff + 1))
        
        return False