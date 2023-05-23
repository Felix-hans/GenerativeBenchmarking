# @lc app=leetcode id=888 lang=python3
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        bob_set = set(bobSizes)
        
        for size in aliceSizes:
            target_size = (sum_bob - sum_alice) // 2 + size
            if target_size in bob_set:
                return [size, target_size]
        
        return []