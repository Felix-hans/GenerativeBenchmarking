# @lc app=leetcode id=2266 lang=python3
class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        mappings = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        n = len(pressedKeys)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(n):
            digit = int(pressedKeys[i])
            letters = mappings[digit]
            for j in range(1, len(letters)+1):
                dp[i+j] = (dp[i+j] + dp[i]) % (10**9 + 7)
        
        return dp[n]