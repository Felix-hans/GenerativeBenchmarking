# @lc app=leetcode id=2406 lang=python3
class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on start values

        groups = []  # List to store the groups
        last_end = float('-inf')  # Keep track of the end value of the last added interval

        for interval in intervals:
            start, end = interval
            if start > last_end:
                groups.append([interval])
                last_end = end

            else:
                for group in groups:
                    if group[-1][1] >= start:
                        group.append(interval)
                        last_end = max(last_end, end)
                        break

        return len(groups)