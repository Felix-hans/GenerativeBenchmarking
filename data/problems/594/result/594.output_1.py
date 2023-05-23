# @lc app=leetcode id=594 lang=python3
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_counts = {}
        max_length = 0

        for num in nums:
            num_counts[num] = num_counts.get(num, 0) + 1

        for num in num_counts:
            if num + 1 in num_counts:
                length = num_counts[num] + num_counts[num + 1]
                max_length = max(max_length, length)

        return max_length