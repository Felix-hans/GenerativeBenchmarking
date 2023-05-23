# @lc app=leetcode id=961 lang=python3
from typing import List

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_count = {}
        n = len(nums) // 2

        for num in nums:
            if num in num_count:
                num_count[num] += 1
                if num_count[num] == n:
                    return num
            else:
                num_count[num] = 1