# @lc app=leetcode id=89 lang=python3
from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        sequence = [0]  # Step 1
        
        mask = 1  # Step 3
        for i in range(n):  # Step 4
            len_seq = len(sequence)
            for j in range(len_seq - 1, -1, -1):
                sequence.append(sequence[j] | mask)
            mask = mask << 1  # Toggle mask
        
        return sequence  # Step 5