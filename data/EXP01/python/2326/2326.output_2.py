# @lc app=leetcode id=2326 lang=python3
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        left = 0
        right = n - 1
        top = 0
        bottom = m - 1
        
        row = 0
        col = 0
        dr = 0
        dc = 1

        for value in values:
            matrix[row][col] = value
            
            if row + dr < top or row + dr > bottom or col + dc < left or col + dc > right:
                if dr == 0 and dc == 1:
                    dr = 1
                    dc = 0
                elif dr == 1 and dc == 0:
                    dr = 0
                    dc = -1
                elif dr == 0 and dc == -1:
                    dr = -1
                    dc = 0
                elif dr == -1 and dc == 0:
                    dr = 0
                    dc = 1
            
            row += dr
            col += dc
        
        return matrix