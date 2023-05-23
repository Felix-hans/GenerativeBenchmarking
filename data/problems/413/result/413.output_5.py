# @lc app=leetcode id=413 lang=python3
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        dp = [0] * n  # Dynamic programming array to store the number of arithmetic slices ending at each index
        count = 0  # Total count of arithmetic slices
        
        for i in range(2, n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
                count += dp[i]
        
        return count