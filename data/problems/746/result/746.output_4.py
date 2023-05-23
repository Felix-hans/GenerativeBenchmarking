# @lc app=leetcode id=746 lang=python3
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1], dp[i - 2]) + (cost[i] if i < n else 0)

        return min(dp[-1], dp[-2])