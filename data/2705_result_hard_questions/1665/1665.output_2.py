# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0]), reverse=True)  # Sort tasks in reverse order of difference between minimum and actual energy

        initial_energy = 0
        total_energy = 0

        for task in tasks:
            actual_energy, minimum_energy = task
            if initial_energy < minimum_energy:
                energy_required = minimum_energy - initial_energy
                initial_energy = minimum_energy
                total_energy += energy_required
            initial_energy -= actual_energy

        return total_energy