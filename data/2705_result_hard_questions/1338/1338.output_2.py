# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq_map = {}
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        frequencies = sorted(freq_map.values(), reverse=True)

        removed = 0
        removed_count = 0
        for freq in frequencies:
            removed += freq
            removed_count += 1
            if removed >= len(arr) // 2:
                break

        return removed_count