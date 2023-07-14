# @lc app=leetcode id=1297 lang=python3
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        counts = defaultdict(int)
        max_occurrences = 0
        
        for i in range(len(s) - minSize + 1):
            substring = s[i:i+minSize]
            unique_letters = len(set(substring))
            
            if unique_letters <= maxLetters:
                counts[substring] += 1
                max_occurrences = max(max_occurrences, counts[substring])
        
        return max_occurrences