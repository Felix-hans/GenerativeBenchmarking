# @lc app=leetcode id=392 lang=python3
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0  # Pointer for string s
        t_pointer = 0  # Pointer for string t
        
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1  # Move s pointer forward
            t_pointer += 1  # Move t pointer forward
        
        return s_pointer == len(s)