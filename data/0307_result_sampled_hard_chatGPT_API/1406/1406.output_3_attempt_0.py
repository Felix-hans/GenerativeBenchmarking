# @lc app=leetcode id=1406 lang=python3
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            max_score = float('-inf')

            for k in range(1, 4):
                if i + k <= n:
                    max_score = max(max_score, sum(stoneValue[i:i+k]) - dp[i+k])
            
            dp[i] = max_score

        if dp[0] > sum(stoneValue) - dp[0]:
            return "Alice"
        elif dp[0] == sum(stoneValue) - dp[0]:
            return "Tie"
        else:
            return "Bob"