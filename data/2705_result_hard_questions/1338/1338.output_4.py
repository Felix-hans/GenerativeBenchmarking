# @lc app=leetcode id=1338 lang=python3
from typing import List
from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = Counter(arr)
        count = 0
        removed = 0
        for num, occurrence in freq.most_common():
            count += 1
            removed += occurrence
            if removed >= len(arr) // 2:
                break
        return count