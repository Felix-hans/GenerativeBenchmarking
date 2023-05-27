# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        sorted_freq = sorted(freq.values(), reverse=True)
        
        count = 0
        removed = 0
        for f in sorted_freq:
            count += 1
            removed += f
            if removed >= len(arr) // 2:
                return count