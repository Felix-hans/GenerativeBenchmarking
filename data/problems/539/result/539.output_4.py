# @lc app=leetcode id=539 lang=python3
from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(':'))
            minutes.append(h * 60 + m)
        
        minutes.sort()
        
        min_diff = float('inf')
        n = len(minutes)
        
        for i in range(1, n):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)
        
        circular_diff = minutes[0] + (24 * 60) - minutes[n - 1]
        min_diff = min(min_diff, circular_diff)
        
        return min_diff