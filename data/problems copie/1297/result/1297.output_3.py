# @lc app=leetcode id=1297 lang=python3
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_counts = defaultdict(int)  # To store the occurrences of valid substrings
        
        max_freq = 0  # Maximum frequency of any valid substring
        
        for i in range(len(s) - minSize + 1):
            substring = s[i:i+minSize]  # Current substring of minimum size
            
            if len(set(substring)) <= maxLetters:  # Check if substring satisfies maxLetters condition
                substr_counts[substring] += 1  # Increment the occurrence count for the substring
                max_freq = max(max_freq, substr_counts[substring])  # Update the maximum frequency
        
        return max_freq