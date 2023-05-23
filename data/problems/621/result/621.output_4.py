# @lc app=leetcode id=621 lang=python3
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = [0] * 26  # Assuming uppercase English letters
        
        for task in tasks:
            task_counts[ord(task) - ord('A')] += 1
        
        task_counts.sort(reverse=True)
        
        max_freq = task_counts[0]
        idle_slots = (max_freq - 1) * n
        
        for count in task_counts[1:]:
            idle_slots -= min(count, max_freq - 1)
        
        idle_slots = max(0, idle_slots)
        
        return len(tasks) + idle_slots