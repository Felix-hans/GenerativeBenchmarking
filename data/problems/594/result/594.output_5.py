# @lc app=leetcode id=594 lang=python3
from typing import List

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_length = 0
        for num in freq:
            if num + 1 in freq:
                length = freq[num] + freq[num + 1]
                max_length = max(max_length, length)

        return max_length