# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)  # Initialize dp array
        
        last = {}  # To store the last occurrence of each character
        dp[0] = 1  # Empty subsequence
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % (10**9 + 7)  # Case 1
            
            if s[i - 1] in last:
                dp[i] -= dp[last[s[i - 1]] - 1]  # Case 2
            last[s[i - 1]] = i
        
        return (dp[n] - 1) % (10**9 + 7)  # Subtract the empty subsequence