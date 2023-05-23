# @lc app=leetcode id=1128 lang=python3
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        pairs = 0

        for domino in dominoes:
            key = tuple(sorted(domino))
            if key in count:
                pairs += count[key]
                count[key] += 1
            else:
                count[key] = 1

        return pairs