# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            min_string = s
            for _ in range(len(s)):
                s = s[1:] + s[0]  # Move the first character to the end
                min_string = min(min_string, s)  # Update the minimum string
            return min_string
        else:
            return ''.join(sorted(s))