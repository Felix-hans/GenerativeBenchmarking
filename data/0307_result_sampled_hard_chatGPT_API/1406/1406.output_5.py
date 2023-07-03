# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take_one = stoneValue[i] - dp[i + 1]
            take_two = sum(stoneValue[i:i + 2]) - dp[i + 2] if i + 2 <= n else float('-inf')
            take_three = sum(stoneValue[i:i + 3]) - dp[i + 3] if i + 3 <= n else float('-inf')

            dp[i] = max(take_one, take_two, take_three)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"