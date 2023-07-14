# @lc app=leetcode id=2358 lang=python3
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)  # Sort the grades in descending order
        groups = []
        current_group_sum = 0
        current_group_count = 0
        
        for grade in grades:
            current_group_sum += grade
            current_group_count += 1
            
            if len(groups) == 0 or current_group_sum < sum(groups[-1]):
                groups.append([grade])
                current_group_sum = grade
                current_group_count = 1
            else:
                groups[-1].append(grade)
        
        return len(groups)