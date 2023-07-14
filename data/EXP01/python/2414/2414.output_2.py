# @lc app=leetcode id=2414 lang=python3
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        maxLength = 0
        currentLength = 1
        for i in range(1, len(s)):
            if ord(s[i]) - ord(s[i-1]) == 1:
                currentLength += 1
            else:
                currentLength = 1
            maxLength = max(maxLength, currentLength)
        return maxLength