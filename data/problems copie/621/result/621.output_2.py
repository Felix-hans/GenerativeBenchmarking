# @lc app=leetcode id=621 lang=python3
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26  # To store the frequency of each task
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        max_freq = max(task_counts)  # Maximum frequency of any task
        max_freq_count = task_counts.count(max_freq)  # Number of tasks with maximum frequency
        
        idle_slots = max((max_freq - 1) * (n + 1), 0)
        
        total_slots = idle_slots + max_freq_count
        
        return max(total_slots, len(tasks))