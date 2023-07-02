# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        last_seen = {}
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i-1]) % (10**9 + 7)
            
            if s[i-1] in last_seen:
                j = last_seen[s[i-1]]
                dp[i] = (dp[i] - dp[j]) % (10**9 + 7)
            
            last_seen[s[i-1]] = i
        
        return dp[n] % (10**9 + 7)