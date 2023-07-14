# @lc app=leetcode id=594 lang=python3
from collections import Counter

class Solution:
    def findLHS(self, nums):
        num_counts = Counter(nums)
        max_length = 0

        for num in num_counts:
            if num + 1 in num_counts:
                length = num_counts[num] + num_counts[num + 1]
                max_length = max(max_length, length)

        return max_length