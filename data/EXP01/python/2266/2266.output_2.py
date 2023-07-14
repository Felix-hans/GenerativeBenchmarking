# @lc app=leetcode id=2266 lang=python3
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mod = 1000000007
        dp = [0] * (len(pressedKeys) + 1)
        dp[0] = 1
        for i in range(1, len(pressedKeys) + 1):
            for j in range(i - 1, -1, -1):
                if pressedKeys[j:i] in {"2", "3", "4", "5", "6", "7", "8", "9"}:
                    dp[i] = (dp[i] + dp[j]) % mod
        return dp[-1]