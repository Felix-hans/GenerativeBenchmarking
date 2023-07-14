# @lc app=leetcode id=621 lang=python3
from collections import Counter
class Solution:
    def leastInterval(self, tasks, n):
        task_counts = Counter(tasks)
        max_freq = max(task_counts.values())
        max_freq_tasks = list(task_counts.values()).count(max_freq)
        intervals = (max_freq - 1) * (n + 1) + max_freq_tasks
        return max(intervals, len(tasks))