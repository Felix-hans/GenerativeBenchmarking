# @lc app=leetcode id=1402 lang=python3
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)  # Sort dishes in descending order

        total_time = 0
        max_coefficient = 0

        for sat in satisfaction:
            if total_time + sat <= 0:
                break
            total_time += sat
            max_coefficient += total_time

        return max_coefficient