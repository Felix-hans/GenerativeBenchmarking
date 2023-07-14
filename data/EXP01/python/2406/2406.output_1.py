# @lc app=leetcode id=2406 lang=python3
from typing import List

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on starting point
        groups = 1  # Initialize the number of groups

        end = intervals[0][1]  # Initialize the end point of the first interval
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:  # If the interval does not overlap with the previous one
                groups += 1  # Start a new group
                end = intervals[i][1]  # Update the end point
            else:
                end = max(end, intervals[i][1])  # Update the end point if the interval overlaps
        
        return groups