# @lc app=leetcode id=1425 lang=python3
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums, k):
        n = len(nums)
        dp = [0] * n
        deque_ = deque()
        max_sum = float('-inf')

        for i in range(n):
            if deque_ and i - deque_[0] > k:
                deque_.popleft()

            dp[i] = nums[i] + max(0, dp[deque_[0]]) if deque_ else nums[i]
            
            while deque_ and dp[i] >= dp[deque_[-1]]:
                deque_.pop()

            deque_.append(i)

            max_sum = max(max_sum, dp[i])

        return max_sum