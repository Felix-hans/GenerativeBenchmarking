# @lc app=leetcode id=467 lang=python3
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        if not s:
            return 0
        
        char_counts = [0] * 26
        lengths = [0] * 26
        
        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            
            if i > 0 and (ord(s[i]) - ord(s[i-1]) == 1 or ord(s[i-1]) - ord(s[i]) == 25):
                lengths[index] = max(lengths[index], lengths[(index - 1) % 26] + 1)
            else:
                lengths[index] = 1
            
            char_counts[index] = max(char_counts[index], lengths[index])
        
        return sum(char_counts)