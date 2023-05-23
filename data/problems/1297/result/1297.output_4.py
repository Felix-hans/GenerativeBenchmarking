# @lc app=leetcode id=1297 lang=python3
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_counts = defaultdict(int)
        max_occurrences = 0

        for i in range(len(s) - minSize + 1):
            substring = s[i:i + minSize]
            unique_chars = set(substring)

            if len(unique_chars) <= maxLetters:
                substring_counts[substring] += 1
                max_occurrences = max(max_occurrences, substring_counts[substring])

        return max_occurrences