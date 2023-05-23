# @lc app=leetcode id=467 lang=python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * 26  # Initialize an array to store the max length of substring ending at each letter
        
        dp[ord(s[0]) - ord('a')] = 1
        length = 1  # Current max length of substring
        
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                length += 1
            else:
                length = 1  # Reset length to 1 if not consecutive
            
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], length)
        
        return sum(dp)