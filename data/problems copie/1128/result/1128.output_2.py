# @lc app=leetcode id=1128 lang=python3
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        pair_counts = {}  # Dictionary to store counts of equivalent pairs
        num_pairs = 0  # Counter for the total number of equivalent pairs
        
        for domino in dominoes:
            domino.sort()
            pair_key = tuple(domino)  # Convert the pair to a tuple for dictionary key
            
            pair_counts[pair_key] = pair_counts.get(pair_key, 0) + 1
            
        for count in pair_counts.values():
            num_pairs += count * (count - 1) // 2
        
        return num_pairs