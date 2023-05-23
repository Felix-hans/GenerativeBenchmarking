# @lc app=leetcode id=1636 lang=python3
from typing import List
from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        return sorted(nums, key=lambda x: (frequency[x], -x))