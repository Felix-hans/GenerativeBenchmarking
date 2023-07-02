# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        
        total_energy = 0
        initial_energy = 0
        
        for task in tasks:
            actual_energy, minimum_energy = task
            total_energy += minimum_energy
            
            if initial_energy < minimum_energy:
                initial_energy = minimum_energy
            
            total_energy -= actual_energy
        
        return max(total_energy, initial_energy)