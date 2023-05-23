# @lc app=leetcode id=1128 lang=python3
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = {}
        pairs = 0
        
        for domino in dominoes:
            key = tuple(sorted(domino))
            count[key] = count.get(key, 0) + 1
        
        for val in count.values():
            pairs += val * (val - 1) // 2
        
        return pairs