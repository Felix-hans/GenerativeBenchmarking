# @lc app=leetcode id=740 lang=python3
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums):
        freq_map = Counter(nums)

        max_num = max(nums)

        prev = curr = 0

        for num in range(max_num + 1):
            points = num * freq_map[num]

            prev, curr = curr, max(prev + points, curr)

        return curr