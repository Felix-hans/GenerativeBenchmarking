# @lc app=leetcode id=89 lang=python3
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        prev_sequence = self.grayCode(n - 1)
        mask = 1 << (n - 1)  # Create a mask to toggle the additional bit
        
        return prev_sequence + [num | mask for num in reversed(prev_sequence)]