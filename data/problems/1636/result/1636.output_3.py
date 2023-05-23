# @lc app=leetcode id=1636 lang=python3
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        sorted_values = sorted(frequency, key=lambda x: (frequency[x], -x))
        result = []
        
        for value in sorted_values:
            result.extend([value] * frequency[value])
        
        return result