# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)  # Sort tasks based on energy difference
        initial_energy = 0
        current_energy = 0
        
        for task in tasks:
            actual_energy, min_energy = task
            if current_energy < min_energy:
                diff = min_energy - current_energy
                initial_energy += diff
                current_energy += diff
            current_energy -= actual_energy
        
        return initial_energy