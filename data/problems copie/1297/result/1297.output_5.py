# @lc app=leetcode id=1297 lang=python3
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_freq = defaultdict(int)  # Store frequency of valid substrings
        max_freq = 0  # Maximum frequency found

        for i in range(len(s) - minSize + 1):
            window = s[i:i+minSize]  # Get the substring of size minSize

            if len(set(window)) <= maxLetters:
                substr_freq[window] += 1  # Increment the frequency of the substring
                max_freq = max(max_freq, substr_freq[window])  # Update the maximum frequency

        return max_freq