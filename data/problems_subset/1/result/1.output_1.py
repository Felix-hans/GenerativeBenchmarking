# @lc app=leetcode id=1 lang=python3
class Solution:
    def twoSum(self, nums, target):
        complement_map = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [complement_map[complement], i]
            
            complement_map[num] = i
        
        return []