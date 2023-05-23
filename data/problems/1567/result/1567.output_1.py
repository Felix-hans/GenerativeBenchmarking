# @lc app=leetcode id=1567 lang=python3
from typing import List

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        positive_count = 0
        negative_count = 0

        for num in nums:
            if num > 0:
                positive_count += 1
                if negative_count > 0:
                    negative_count += 1
            elif num < 0:
                temp = positive_count
                positive_count = negative_count + 1
                negative_count = temp + 1
            else:
                positive_count = 0
                negative_count = 0

            max_len = max(max_len, positive_count)

        return max_len