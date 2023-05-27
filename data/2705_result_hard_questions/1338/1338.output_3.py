# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = {}
        for num in arr:
            frequency[num] = frequency.get(num, 0) + 1
        
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        count = 0
        removed = 0
        for num, freq in sorted_freq:
            count += 1
            removed += freq
            if removed >= len(arr) // 2:
                break
        
        return count