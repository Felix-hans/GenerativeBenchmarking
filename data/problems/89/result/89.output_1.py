# @lc app=leetcode id=89 lang=python3
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        gray_code = [0]  # Initialize with 0
        mask = 1  # Initialize mask

        for i in range(n):
            for j in range(len(gray_code) - 1, -1, -1):
                next_gray_code = gray_code[j] | mask  # Toggle the bit at position i
                gray_code.append(next_gray_code)

            mask <<= 1  # Update the mask by left-shifting

        return gray_code