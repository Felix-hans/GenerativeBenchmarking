# @lc app=leetcode id=1425 lang=python3
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        result = float('-inf')
        max_sum = float('-inf')
        
        for i in range(n):
            if i <= k:
                max_sum = max(max_sum, 0)
            else:
                max_sum = max(max_sum, dp[i-k-1])
            
            dp[i] = max(max_sum + nums[i], nums[i])
            
            result = max(result, dp[i])
        
        return result