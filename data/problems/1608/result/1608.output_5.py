# @lc app=leetcode id=1608 lang=python3
from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            if num >= n:
                count[n] += 1
            else:
                count[num] += 1

        curr_count = 0
        for i in range(n, -1, -1):
            curr_count += count[i]
            if curr_count == i:
                return i

        return -1