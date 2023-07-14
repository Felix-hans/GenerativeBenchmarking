# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0])  # Sort tasks based on the energy difference

        total_energy = 0
        initial_energy = 0

        for task in tasks:
            actual_energy, minimum_energy = task
            if initial_energy < minimum_energy:
                energy_diff = minimum_energy - initial_energy
                total_energy += energy_diff
                initial_energy = minimum_energy
            initial_energy -= actual_energy

        return total_energy