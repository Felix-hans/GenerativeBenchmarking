# @lc app=leetcode id=1297 lang=python3
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq_count = defaultdict(int)
        max_freq = 0
        left = 0
        unique_chars = set()

        for right in range(len(s) - minSize + 1):
            sub_str = s[right:right+minSize]

            while len(sub_str) <= maxSize and left + minSize <= len(s):
                if len(set(sub_str)) <= maxLetters:
                    freq_count[sub_str] += 1
                    max_freq = max(max_freq, freq_count[sub_str])

                left += 1
                unique_chars.remove(s[left-1])
                if s[left-1] not in freq_count or freq_count[s[left-1]] == 0:
                    sub_str = sub_str[1:]
                freq_count[s[left-1]] -= 1

            right += 1
            if right < len(s):
                unique_chars.add(s[right])
                sub_str += s[right]

        return max_freq