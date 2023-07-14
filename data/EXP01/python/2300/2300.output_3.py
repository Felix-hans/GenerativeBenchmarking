# @lc app=leetcode id=2300 lang=python3
from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = [0] * len(spells) # Initialize the result list with zeros
        
        potions.sort() # Sort the potions array in ascending order
        
        for i, spell in enumerate(spells):
            left, right = 0, len(potions) - 1 # Pointers for left and right ends of potions array
            
            while left <= right:
                mid = (left + right) // 2
                if spell * potions[mid] >= success:
                    pairs[i] += len(potions) - mid
                    right = mid - 1
                else:
                    left = mid + 1
        
        return pairs