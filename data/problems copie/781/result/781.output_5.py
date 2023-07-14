# @lc app=leetcode id=781 lang=python3
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count_map = {}  # Hash map to store the counts of rabbits with each color
        
        for answer in answers:
            if answer not in count_map:
                count_map[answer] = 1
            else:
                count_map[answer] += 1
        
        min_rabbits = 0
        
        for answer, count in count_map.items():
            groups = count // (answer + 1)  # Number of groups with rabbits of the same color
            remainder = count % (answer + 1)  # Remaining rabbits
            
            if remainder > 0:
                groups += 1
            
            min_rabbits += groups * (answer + 1)
        
        return min_rabbits