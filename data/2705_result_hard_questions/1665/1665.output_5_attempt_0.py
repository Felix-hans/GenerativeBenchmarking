# @lc app=leetcode id=1665 lang=python3
class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)
        
        min_energy = 0
        current_energy = 0
        
        for task in tasks:
            actual_energy, min_required_energy = task
            
            if current_energy < min_required_energy:
                diff = min_required_energy - current_energy
                min_energy += diff
                current_energy += diff
            
            current_energy -= actual_energy
        
        return min_energy + current_energy