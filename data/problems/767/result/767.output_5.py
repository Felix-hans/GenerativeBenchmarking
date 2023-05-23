# @lc app=leetcode id=767 lang=python3
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        most_common = counter.most_common()  # List of (char, freq) tuples, sorted by frequency

        max_freq = most_common[0][1]
        if max_freq > (len(s) + 1) // 2:
            return ""

        result = [''] * len(s)
        index = 0

        for char, freq in most_common:
            for _ in range(freq):
                result[index] = char
                index += 2  # Skip one index to avoid adjacent characters
                if index >= len(s):
                    index = 1  # If we reach the end, start from index 1
        return "".join(result)