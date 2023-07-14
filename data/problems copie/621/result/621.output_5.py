# @lc app=leetcode id=621 lang=python3
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_tasks = sum(1 for count in task_counts.values() if count == max_freq)
        number_of_slots = (max_freq - 1) * n
        total_slots = max(number_of_slots + max_freq + max_freq_tasks - 1, len(tasks))
        return total_slots