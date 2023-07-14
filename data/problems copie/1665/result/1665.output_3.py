# @lc app=leetcode id=1665 lang=python3
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)  # Sort tasks in descending order based on the difference
        
        initial_energy = 0
        current_energy = 0
        
        for task in tasks:
            actual_energy, minimum_energy = task
            if current_energy < minimum_energy:
                initial_energy += minimum_energy - current_energy
                current_energy = minimum_energy
            current_energy -= actual_energy
        
        return initial_energy