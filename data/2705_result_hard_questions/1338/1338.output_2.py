# @lc app=leetcode id=1338 lang=python3
from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency_map = Counter(arr)
        sorted_frequencies = sorted(frequency_map.values(), reverse=True)
        
        count = 0
        removed = 0
        for frequency in sorted_frequencies:
            removed += frequency
            count += 1
            if removed >= len(arr) // 2:
                break
        
        return count