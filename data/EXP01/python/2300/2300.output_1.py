# @lc app=leetcode id=2300 lang=python3
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []
        for spell in spells:
            count = 0
            for potion in potions:
                if spell * potion >= success:
                    count += 1
            pairs.append(count)
        return pairs