# @lc app=leetcode id=283 lang=python3
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_ptr = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero_ptr] = nums[non_zero_ptr], nums[i]
                non_zero_ptr += 1