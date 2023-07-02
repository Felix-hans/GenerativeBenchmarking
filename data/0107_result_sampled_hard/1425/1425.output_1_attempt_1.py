# @lc app=leetcode id=1425 lang=python3
from typing import List
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        queue = deque()  # Stores the indices of the potential subsequence
        max_sum = float('-inf')

        for i in range(n):
            while queue and queue[0] < i - k:
                queue.popleft()

            max_prev_sum = max(0, dp[j] for j in queue)

            dp[i] = max_prev_sum + nums[i]
            queue.append(i)

            max_sum = max(max_sum, dp[i])

        return max_sum