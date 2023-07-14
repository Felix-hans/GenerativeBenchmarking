# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            rotations = [s[i:] + s[:i] for i in range(len(s))]
            return min(rotations)
        else:
            return ''.join(sorted(s))