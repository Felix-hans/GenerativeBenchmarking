# @lc app=leetcode id=1128 lang=python3
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        pairs = 0

        for domino in dominoes:
            domino.sort()

            domino_tuple = tuple(domino)

            count[domino_tuple] = count.get(domino_tuple, 0) + 1

            pairs += count[domino_tuple] - 1

        return pairs