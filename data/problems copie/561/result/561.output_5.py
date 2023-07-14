# @lc app=leetcode id=561 lang=python3
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the array
        
        max_sum = 0  # Step 2: Initialize the maximum sum
        
        for i in range(0, len(nums), 2):
            max_sum += min(nums[i], nums[i + 1])
        
        return max_sum  # Step 5