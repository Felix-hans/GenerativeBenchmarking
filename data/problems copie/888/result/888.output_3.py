# @lc app=leetcode id=888 lang=python3
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_alice = sum(aliceSizes)
        sum_bob = sum(bobSizes)
        diff = sum_bob - sum_alice

        set_bob = set(bobSizes)

        for candy in aliceSizes:
            target = candy + diff // 2
            if target in set_bob:
                return [candy, target]

        return []  # No valid answer found