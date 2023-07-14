# @lc app=leetcode id=76 lang=python3
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1

        window_start = 0
        window_end = 0
        min_length = float('inf')
        min_window = ""
        count = len(t_count)

        while window_end < len(s):
            char = s[window_end]

            if char in t_count:
                t_count[char] -= 1
                if t_count[char] == 0:
                    count -= 1

            while count == 0:
                if window_end - window_start + 1 < min_length:
                    min_length = window_end - window_start + 1
                    min_window = s[window_start:window_end+1]

                left_char = s[window_start]
                if left_char in t_count:
                    t_count[left_char] += 1
                    if t_count[left_char] > 0:
                        count += 1
                window_start += 1

            window_end += 1

        return min_window