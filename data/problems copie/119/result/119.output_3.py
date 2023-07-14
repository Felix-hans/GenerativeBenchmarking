# @lc app=leetcode id=119 lang=python3
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Start with the first row [1]
        
        for i in range(1, rowIndex + 1):
            next_row = [1]
            
            for j in range(1, i):
                next_row.append(row[j - 1] + row[j])
            
            next_row.append(1)
            row = next_row
        
        return row