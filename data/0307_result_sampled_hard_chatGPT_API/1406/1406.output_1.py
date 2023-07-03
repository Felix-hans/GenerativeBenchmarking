# @lc app=leetcode id=1406 lang=python3
class Solution:
    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)
        dp = [0] * (n + 1) # dp[i] represents the maximum possible score difference Alice can achieve starting from the i-th stone
        
        for i in range(n-1, -1, -1):
            choose = float('-inf')
            for k in [1, 2, 3]:
                if i + k <= n:
                    choose = max(choose, sum(stoneValue[i:i+k]) - dp[i+k])
            dp[i] = choose
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"