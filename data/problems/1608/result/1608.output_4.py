# @lc app=leetcode id=1608 lang=python3
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        for x in range(n+1):
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return -1