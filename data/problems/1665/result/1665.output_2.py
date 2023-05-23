# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        initial_energy = 0
        
        for task in tasks:
            actual, minimum = task
            if initial_energy < minimum:
                initial_energy += minimum - initial_energy
            initial_energy -= actual
        
        return initial_energy