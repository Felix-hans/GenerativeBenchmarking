# @lc app=leetcode id=2522 lang=python3
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        
        substr = ""
        value = 0
        count = 0
        
        for i in range(n):
            digit = int(s[i])
            
            if value + digit > k:
                substr = ""
                value = 0
                count += 1
            
            substr += s[i]
            value += digit
        
        if substr:
            count += 1
        
        if count == 0:
            return -1
        
        return count