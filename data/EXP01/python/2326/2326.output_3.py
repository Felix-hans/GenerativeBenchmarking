# @lc app=leetcode id=2326 lang=python3
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction = 0
        
        row, col = 0, 0
        
        while head:
            matrix[row][col] = head.val
            
            dx, dy = directions[direction]
            next_row, next_col = row + dx, col + dy
            
            if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n or matrix[next_row][next_col] != -1:
                direction = (direction + 1) % 4
                dx, dy = directions[direction]
                next_row, next_col = row + dx, col + dy
            
            row, col = next_row, next_col
            head = head.next
        
        return matrix