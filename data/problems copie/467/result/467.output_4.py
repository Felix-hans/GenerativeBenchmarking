# @lc app=leetcode id=467 lang=python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * 26
        
        dp[ord(s[0]) - ord('a')] = 1
        curr_length = 1
        
        for i in range(1, len(s)):
            if (ord(s[i]) - ord(s[i-1])) % 26 == 1:
                curr_length += 1
            else:
                curr_length = 1
            
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], curr_length)
        
        return sum(dp)