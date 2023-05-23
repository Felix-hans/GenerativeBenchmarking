# @lc app=leetcode id=1665 lang=python3
from typing import List

class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)
        total_energy = 0
        initial_energy = 0

        for actual, minimum in tasks:
            if initial_energy < minimum:
                diff = minimum - initial_energy
                total_energy += diff
                initial_energy += diff
            initial_energy -= actual

        return total_energy