# @lc app=leetcode id=1608 lang=python3
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        counts = [0] * (n + 1)  # Initialize counts array with zeros

        for num in nums:
            if num <= n:
                counts[num] += 1
            else:
                counts[n] += 1

        greater_count = 0
        for i in range(n, -1, -1):
            greater_count += counts[i]
            if greater_count == i:
                return i

        return -1