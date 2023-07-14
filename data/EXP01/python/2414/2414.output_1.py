# @lc app=leetcode id=2414 lang=python3
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        longest_length = 0
        current_length = 0

        for i in range(len(s)):
            if i > 0 and ord(s[i]) - ord(s[i-1]) != 1:
                current_length = 0
            current_length += 1
            longest_length = max(longest_length, current_length)

        return longest_length