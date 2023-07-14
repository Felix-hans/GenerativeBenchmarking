# @lc app=leetcode id=1338 lang=python3
from typing import List

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}  # Dictionary to store the frequency of integers
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        sorted_freq = sorted(freq.values(), reverse=True)  # Sort frequencies in descending order

        count = 0  # Number of integers removed
        removed = 0  # Total number of integers removed
        half_len = len(arr) // 2

        for f in sorted_freq:
            count += 1
            removed += f
            if removed >= half_len:
                break

        return count