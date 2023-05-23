# @lc app=leetcode id=781 lang=python3
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = {}  # Dictionary to store the counts of each answer
        
        for ans in answers:
            if ans not in counts:
                counts[ans] = 1
            else:
                counts[ans] += 1
        
        total_rabbits = 0
        
        for ans, count in counts.items():
            groups = count // (ans + 1)
            if count % (ans + 1) != 0:
                groups += 1
            total_rabbits += groups * (ans + 1)
        
        return total_rabbits