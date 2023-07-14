# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            n = len(s)
            smallest = s
            for _ in range(n):
                s = s[1:] + s[0]
                if s < smallest:
                    smallest = s
            return smallest
        else:
            return "".join(sorted(s))