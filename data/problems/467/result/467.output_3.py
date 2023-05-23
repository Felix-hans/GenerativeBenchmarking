# @lc app=leetcode id=467 lang=python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * 26  # Initialize counts for each letter
        
        length = 1  # Length of the current substring
        dp[ord(s[0]) - ord('a')] = 1  # Update count for the first letter
        
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25:
                length += 1
            else:
                length = 1
            
            letter_index = ord(s[i]) - ord('a')
            dp[letter_index] = max(dp[letter_index], length)
        
        return sum(dp)