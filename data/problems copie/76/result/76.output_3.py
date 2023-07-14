# @lc app=leetcode id=76 lang=python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_freq = {}
        for char in t:
            target_freq[char] = target_freq.get(char, 0) + 1
        
        window_start = 0
        window_end = 0
        window_freq = {}
        formed = 0  # Number of characters in t that have been formed in the window
        
        min_window_length = float('inf')
        min_window_start = 0
        
        while window_end < len(s):
            char = s[window_end]
            window_freq[char] = window_freq.get(char, 0) + 1
            
            if char in target_freq and window_freq[char] <= target_freq[char]:
                formed += 1
            
            while formed == len(t):
                if window_end - window_start + 1 < min_window_length:
                    min_window_length = window_end - window_start + 1
                    min_window_start = window_start
                
                char = s[window_start]
                window_freq[char] -= 1
                
                if char in target_freq and window_freq[char] < target_freq[char]:
                    formed -= 1
                
                window_start += 1  # Move the window start to the right
            
            window_end += 1  # Move the window end to the right
        
        if min_window_length == float('inf'):
            return ""
        
        return s[min_window_start:min_window_start + min_window_length]