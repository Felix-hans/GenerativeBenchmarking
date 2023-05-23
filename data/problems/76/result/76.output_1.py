# @lc app=leetcode id=76 lang=python3
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        required_chars = len(t_count)
        
        window_start = 0
        window_chars = {}
        formed_chars = 0
        min_length = float('inf')
        result = ""
        
        for window_end in range(len(s)):
            right_char = s[window_end]
            window_chars[right_char] = window_chars.get(right_char, 0) + 1
            
            if right_char in t_count and window_chars[right_char] == t_count[right_char]:
                formed_chars += 1
            
            while formed_chars == required_chars and window_start <= window_end:
                left_char = s[window_start]
                
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    result = s[window_start:window_end+1]
                
                window_chars[left_char] -= 1
                if left_char in t_count and window_chars[left_char] < t_count[left_char]:
                    formed_chars -= 1
                
                window_start += 1
        
        return result