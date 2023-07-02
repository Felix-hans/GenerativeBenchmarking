# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        total_energy = 0
        current_energy = 0
        
        for task in tasks:
            actual, minimum = task
            if current_energy < minimum:
                energy_diff = minimum - current_energy
                total_energy += energy_diff
                current_energy += energy_diff
            current_energy -= actual
        
        return total_energy