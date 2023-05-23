# @lc app=leetcode id=1122 lang=python3
from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index_map = {num: i for i, num in enumerate(arr2)}
        
        arr1.sort(key=lambda x: index_map.get(x, len(arr2) + x))
        
        return arr1