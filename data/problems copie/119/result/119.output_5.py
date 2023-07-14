# @lc app=leetcode id=119 lang=python3
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            next_row = [1]  # The first element is always 1

            for j in range(1, len(row)):
                next_row.append(row[j-1] + row[j])

            next_row.append(1)  # The last element is always 1
            row = next_row

        return row