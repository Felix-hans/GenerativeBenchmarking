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
        
        top, bottom, left, right = 0, m-1, 0, n-1
        row, col = 0, 0
        direction = 0
        
        for i in range(m * n):
            if direction == 0: # Move right
                matrix[row][col] = values[i]
                col += 1
                if col > right:
                    direction = (direction + 1) % 4
                    top += 1
            elif direction == 1: # Move down
                matrix[row][col] = values[i]
                row += 1
                if row > bottom:
                    direction = (direction + 1) % 4
                    right -= 1
            elif direction == 2: # Move left
                matrix[row][col] = values[i]
                col -= 1
                if col < left:
                    direction = (direction + 1) % 4
                    bottom -= 1
            elif direction == 3: # Move up
                matrix[row][col] = values[i]
                row -= 1
                if row < top:
                    direction = (direction + 1) % 4
                    left += 1
        
        return matrix