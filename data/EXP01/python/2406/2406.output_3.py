# @lc app=leetcode id=2406 lang=python3
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
        groups = 0
        start = end = intervals[0][0]
        
        for interval in intervals:
            if interval[0] > end:
                start = interval[0]
                end = interval[1]
                groups += 1
            else:
                end = max(end, interval[1])
        
        return groups + 1  # Add 1 to include the last group