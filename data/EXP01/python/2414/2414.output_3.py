# @lc app=leetcode id=2414 lang=python3
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        max_len = 0
        left = 0
        right = 0
        
        while right < len(s):
            if right > 0 and ord(s[right]) <= ord(s[right-1]):
                left = right
            right += 1
            max_len = max(max_len, right - left)
        
        return max_len