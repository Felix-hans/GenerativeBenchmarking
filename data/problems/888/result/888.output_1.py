# @lc app=leetcode id=888 lang=python3
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        diff = alice_total - bob_total
        
        bob_set = set(bobSizes)
        
        for candy in aliceSizes:
            target = candy - diff // 2
            if target in bob_set:
                return [candy, target]