# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        frequencies = sorted(counts.values(), reverse=True)

        total_removed = 0
        for i, freq in enumerate(frequencies):
            total_removed += freq
            if total_removed >= len(arr) // 2:
                return i + 1

        return len(arr) // 2  # In case the loop completes without reaching half of the array size