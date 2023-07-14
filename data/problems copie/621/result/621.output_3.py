# @lc app=leetcode id=621 lang=python3
from collections import Counter
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)  # Count the frequency of each task
        max_count = max(task_counts.values())  # Find the task with the maximum frequency
        max_tasks = sum(1 for count in task_counts.values() if count == max_count)

        intervals = (max_count - 1) * (n + 1) + max_tasks

        return max(intervals, len(tasks))