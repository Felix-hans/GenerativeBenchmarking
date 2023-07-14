# @lc app=leetcode id=2358 lang=python3
from typing import List

class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        grades.sort(reverse=True)  # Sort the grades in descending order
        
        groups = []
        current_group_sum = 0
        current_group_count = 0
        
        for grade in grades:
            if current_group_sum + grade >= current_group_count + 1:
                groups.append(current_group_sum)
                current_group_sum = grade
                current_group_count = 1
            else:
                current_group_sum += grade
                current_group_count += 1
                
        groups.append(current_group_sum)  # Add the sum of the last group
        
        return len(groups)