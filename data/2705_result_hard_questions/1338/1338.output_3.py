# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        sorted_freq = sorted(frequency.values(), reverse=True)
        
        target_size = len(arr) // 2
        removed = 0
        num_removed = 0
        for freq in sorted_freq:
            removed += freq
            num_removed += 1
            if removed >= target_size:
                break
        
        return num_removed