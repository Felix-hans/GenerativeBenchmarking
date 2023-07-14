# @lc app=leetcode id=2380 lang=python3
class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        count = 0
        
        for i in range(len(s)):
            if s[i:i+2] == "01":
                count += 1
        
        seconds = count * 2
        
        if count % 2 != 0:
            seconds += 1
        
        return seconds