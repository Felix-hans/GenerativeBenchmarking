# @lc app=leetcode id=76 lang=python3
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        target_counts = Counter(t)
        
        window_counts = {}
        left = right = 0
        formed = 0
        
        min_length = float('inf')
        min_window = ""
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            if char in target_counts and window_counts[char] == target_counts[char]:
                formed += 1
            
            while left <= right and formed == len(target_counts):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    min_window = s[left:right+1]
                
                char = s[left]
                window_counts[char] -= 1
                
                if char in target_counts and window_counts[char] < target_counts[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
        
        return min_window