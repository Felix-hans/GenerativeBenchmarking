# @lc app=leetcode id=1338 lang=python3
from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)

        sorted_freq = sorted(freq.values(), reverse=True)

        removed_count = 0
        removed_set_count = 0
        for count in sorted_freq:
            removed_count += count
            removed_set_count += 1

            if removed_count >= len(arr) // 2:
                break

        return removed_set_count