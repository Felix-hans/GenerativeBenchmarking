# @lc app=leetcode id=1425 lang=python3
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        result = float('-inf')
        
        for i in range(n):
            max_sum = max(dp[max(0, i-k):i]) if i > k else 0
            
            dp[i] = max(max_sum + nums[i], nums[i])
            
            result = max(result, dp[i])
        
        return result