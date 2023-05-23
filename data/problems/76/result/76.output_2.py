# @lc app=leetcode id=76 lang=python3
from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        target_counts = Counter(t)

        window_start = 0
        window_end = 0
        min_window = ""
        min_length = float('inf')
        remaining_chars = len(t)

        while window_end < len(s):
            if s[window_end] in target_counts:
                if target_counts[s[window_end]] > 0:
                    remaining_chars -= 1
                target_counts[s[window_end]] -= 1

            while remaining_chars == 0:
                if window_end - window_start + 1 < min_length:
                    min_window = s[window_start:window_end + 1]
                    min_length = window_end - window_start + 1

                if s[window_start] in target_counts:
                    target_counts[s[window_start]] += 1
                    if target_counts[s[window_start]] > 0:
                        remaining_chars += 1
                window_start += 1

            window_end += 1

        return min_window