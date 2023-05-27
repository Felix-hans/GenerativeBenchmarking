# @lc app=leetcode id=1425 lang=python3
from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n  # dp[i] represents the maximum sum of subsequence ending at index i
        dq = deque()  # Deque to store the indices of potential elements in the subsequence
        max_sum = float('-inf')  # Variable to keep track of the maximum sum
        
        for i in range(n):
            if dq and dq[0] < i - k:
                dq.popleft()
            
            dp[i] = nums[i] + max(0, dp[dq[0]]) if dq else nums[i]
            
            while dq and dp[i] >= dp[dq[-1]]:
                dq.pop()
            
            dq.append(i)  # Add the current index to the deque
            
            max_sum = max(max_sum, dp[i])  # Update the overall maximum sum
        
        return max_sum