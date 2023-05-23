# @lc app=leetcode id=940 lang=python3
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7  # Modulo value
        
        n = len(s)  # Length of the input string
        dp = [0] * (n + 1)  # Initialize an array to store the dynamic programming values
        last = {}  # Dictionary to store the last occurrence index of each character
        
        dp[0] = 1  # Base case
        
        for i in range(1, n + 1):
            dp[i] = (dp[i - 1] * 2) % mod  # The number of subsequences without the current character
            
            if s[i - 1] in last:
                dp[i] -= dp[last[s[i - 1]] - 1]  # Subtract the number of subsequences that end before the last occurrence of the current character
                
            last[s[i - 1]] = i  # Update the last occurrence index of the current character
        
        result = dp[n] - 1 if dp[n] > 0 else 0
        
        return result