# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k >= 2:
            return ''.join(sorted(s))
        
        min_rotation = s
        n = len(s)
        
        for i in range(1, n):
            rotation = s[i:] + s[:i]
            if rotation < min_rotation:
                min_rotation = rotation
        
        return min_rotation