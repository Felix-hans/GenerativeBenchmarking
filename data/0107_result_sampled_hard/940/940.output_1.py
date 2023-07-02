# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        
        dp[0] = 1
        
        last_occurrence = {}
        
        for i, ch in enumerate(s, start=1):
            dp[i] = (2 * dp[i - 1]) % (10**9 + 7)
            
            if ch in last_occurrence:
                dp[i] -= dp[last_occurrence[ch] - 1]
            
            last_occurrence[ch] = i
        
        return (dp[-1] - 1) % (10**9 + 7)