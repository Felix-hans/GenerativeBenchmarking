# @lc app=leetcode id=2380 lang=python3
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        count = 0
        flag = True

        for c in s:
            if c == '0' and flag:
                flag = False
            elif c == '1' and not flag:
                count += 1
                flag = True

        return count