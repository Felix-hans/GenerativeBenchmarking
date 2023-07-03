# @lc app=leetcode id=1406 lang=python3
from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n+1)

        for i in range(n-1, -1, -1):
            take = [0] * 3
            for j in range(3):
                if i+j < n:
                    take[j] = stoneValue[i+j] + dp[i+j+1]
            dp[i] = max(take) - min(take)

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

values = [1, 2, 3, 7]
sol = Solution()
print(sol.stoneGameIII(values))  # Output: "Bob"

values = [1, 2, 3, -9]
print(sol.stoneGameIII(values))  # Output: "Alice"

values = [1, 2, 3, 6]
print(sol.stoneGameIII(values))  # Output: "Tie"