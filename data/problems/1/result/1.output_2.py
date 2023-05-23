# @lc app=leetcode id=1 lang=python3
class Solution:
    def twoSum(self, nums, target):
        complement_dict = {}
        
        for i, num in enumerate(nums):
            if num in complement_dict:
                return [complement_dict[num], i]
            
            complement_dict[target - num] = i
        
        return []