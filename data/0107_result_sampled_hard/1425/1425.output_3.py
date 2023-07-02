# @lc app=leetcode id=1425 lang=python3
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n  # dp[i] stores the maximum sum of a subsequence ending at index i
        
        dq = deque()
        
        max_sum = float('-inf')  # Initialize max_sum with negative infinity
        
        for i in range(n):
            while dq and i - dq[0] > k:
                dq.popleft()
            
            dp[i] = max(nums[i], nums[i] + (dp[dq[0]] if dq else 0))
            
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            dq.append(i)  # Add the current index to the deque
            
            max_sum = max(max_sum, dp[i])  # Update the maximum sum if necessary
        
        return max_sum