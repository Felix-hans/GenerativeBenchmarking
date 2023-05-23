# @lc app=leetcode id=628 lang=python3
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])