# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return ''.join(sorted(s))
        
        smallest = s
        for i in range(len(s)):
            rotated = s[i:] + s[:i]
            if rotated < smallest:
                smallest = rotated
        
        return smallest