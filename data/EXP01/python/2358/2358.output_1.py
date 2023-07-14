# @lc app=leetcode id=2358 lang=python3
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)  # Sort the array in descending order

        groups = 1  # Number of groups formed
        prev_sum = grades[0]  # Sum of grades in the previous group

        for i in range(1, len(grades)):
            if grades[i] * (i+1) > prev_sum:
                groups += 1
                prev_sum += grades[i]
                
        return groups