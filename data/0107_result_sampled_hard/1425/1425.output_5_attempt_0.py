# @lc app=leetcode id=1425 lang=python3
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        result = float('-inf')
        
        for i in range(n):
            start = max(0, i - k)
            max_sum = max(dp[start:i]) if start != 0 else 0
            
            dp[i] = max(max_sum + nums[i], nums[i])
            
            result = max(result, dp[i])
        
        return result