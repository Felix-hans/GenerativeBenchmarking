# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            smallest_string = s
            for i in range(1, len(s)):
                rotated_string = s[i:] + s[:i]
                if rotated_string < smallest_string:
                    smallest_string = rotated_string
            return smallest_string
        else:
            return ''.join(sorted(s))