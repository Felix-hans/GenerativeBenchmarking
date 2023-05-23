# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1
        
        frequencies = sorted(counts.values(), reverse=True)
        removed = 0
        min_size = 0
        
        for freq in frequencies:
            removed += freq
            min_size += 1
            if removed >= len(arr) // 2:
                break
        
        return min_size