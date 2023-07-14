# @lc app=leetcode id=1567 lang=python3
from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        neg_count = 0
        first_neg_idx = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                neg_count = 0
                first_neg_idx = i + 1
            elif nums[i] < 0:
                neg_count += 1
                if neg_count == 1:
                    first_neg_idx = i
            if neg_count % 2 == 0:
                max_len = max(max_len, i - first_neg_idx + 1)

        return max_len