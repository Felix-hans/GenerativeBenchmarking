# @lc app=leetcode id=747 lang=python3
class Solution:
    def dominantIndex(self, nums):
        max_val = max(nums)
        max_index = nums.index(max_val)
        
        for num in nums:
            if num != max_val and max_val < 2 * num:
                return -1
        
        return max_index