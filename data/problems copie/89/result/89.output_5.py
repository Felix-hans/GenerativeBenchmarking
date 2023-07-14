# @lc app=leetcode id=89 lang=python3
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        prev_gray_code = self.grayCode(n - 1)
        
        result = prev_gray_code + [2**(n-1) + x for x in reversed(prev_gray_code)]
        
        return result