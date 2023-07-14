# @lc app=leetcode id=1425 lang=python3
class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        max_sum = dp[0]
        
        for i in range(1, n):
            max_val = max(dp[i-k:i]) if i > k else max(dp[:i])
            dp[i] = max(nums[i], max_val + nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum