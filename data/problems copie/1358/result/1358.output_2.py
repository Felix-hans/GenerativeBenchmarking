# @lc app=leetcode id=1358 lang=python3
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        a_ptr, b_ptr, c_ptr = -1, -1, -1
        n = len(s)
        
        for i in range(n):
            if s[i] == 'a':
                a_ptr = i
            elif s[i] == 'b':
                b_ptr = i
            else:
                c_ptr = i
            
            if a_ptr != -1 and b_ptr != -1 and c_ptr != -1:
                min_ptr = min(a_ptr, b_ptr, c_ptr)
                count += min_ptr + 1  # Add the count of substrings ending at the minimum pointer
         
        return count