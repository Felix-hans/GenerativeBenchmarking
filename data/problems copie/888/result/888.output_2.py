# @lc app=leetcode id=888 lang=python3
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        alice_total = sum(aliceSizes)
        bob_total = sum(bobSizes)
        alice_set = set(aliceSizes)

        for bob_candy in bobSizes:
            target_candy = (alice_total - bob_total) // 2 + bob_candy
            if target_candy in alice_set:
                return [target_candy, bob_candy]