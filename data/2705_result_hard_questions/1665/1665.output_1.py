# @lc app=leetcode id=1665 lang=python3
class Solution:
    def minimumEffort(self, tasks):
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        energy = 0
        initial_energy = 0
        
        for task in tasks:
            actual_energy, minimum_energy = task
            if energy < minimum_energy:
                initial_energy += minimum_energy - energy
                energy = minimum_energy
            energy -= actual_energy
        
        return initial_energy