# @lc app=leetcode id=1425 lang=python3
from collections import deque

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [0] * n
        queue = deque()
        max_sum = float('-inf')

        for i in range(n):
            while queue and i - queue[0] > k:
                queue.popleft()

            dp[i] = max(nums[i], nums[i] + (dp[queue[0]] if queue else 0))

            while queue and dp[i] >= dp[queue[-1]]:
                queue.pop()

            queue.append(i)

            max_sum = max(max_sum, dp[i])

        return max_sum