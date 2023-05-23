# @lc app=leetcode id=53 lang=python3
class Solution:
    def maxSubArray(self, nums):
        max_sum = nums[0]  # Initialize the maximum sum as the first element
        current_sum = nums[0]  # Initialize the current sum as the first element

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum