# @lc app=leetcode id=539 lang=python3
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [self.convertToMinutes(time) for time in timePoints]
        
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(n):
            diff = minutes[(i + 1) % n] - minutes[i]
            if diff < 0:
                diff += 24 * 60  # Add 24 hours in minutes
            min_diff = min(min_diff, diff)
        
        return min_diff
    
    def convertToMinutes(self, time: str) -> int:
        hours, minutes = map(int, time.split(':'))
        return hours * 60 + minutes