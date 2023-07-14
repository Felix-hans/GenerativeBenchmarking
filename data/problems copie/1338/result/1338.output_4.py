# @lc app=leetcode id=1338 lang=python3
from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = Counter(arr)

        sorted_freq = sorted(frequency.values(), reverse=True)

        target_size = len(arr) // 2
        set_size = 0
        removed_count = 0
        for freq in sorted_freq:
            removed_count += freq
            set_size += 1
            if removed_count >= target_size:
                break

        return set_size