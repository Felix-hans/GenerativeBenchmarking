# @lc app=leetcode id=899 lang=python3
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            smallest_char = min(s)
            
            for i in range(len(s)):
                if s[i] == smallest_char:
                    s = s[i:] + s[:i]
                    break
        else:
            s = ''.join(sorted(s))
        
        return s