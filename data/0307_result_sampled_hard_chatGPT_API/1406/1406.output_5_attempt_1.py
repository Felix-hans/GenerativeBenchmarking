# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')] * (n + 1)
        dp[n] = 0

        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[i + 1]
            if i + 1 < n:
                take_two = sum(stoneValue[i:i + 2]) - dp[i + 2]
            else:
                take_two = stoneValue[i]

            take_three = sum(stoneValue[i:i + 3]) - dp[i + 3]

            dp[i] = max(take_one, take_two, take_three)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"