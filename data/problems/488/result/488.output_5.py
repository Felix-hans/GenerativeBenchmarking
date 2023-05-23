# @lc app=leetcode id=488 lang=python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_count = self.countBalls(hand)
        return self.backtrack(board, hand_count)
    
    def countBalls(self, balls: str) -> dict:
        count = {}
        for ball in balls:
            count[ball] = count.get(ball, 0) + 1
        return count
    
    def backtrack(self, board: str, hand_count: dict) -> int:
        if not board:
            return 0  # All balls cleared, return 0
        
        min_steps = float('inf')  # Initialize with a large value
        
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1
            
            color = board[i]
            needed = 3 - (j - i)  # Number of balls needed to form a group of 3
            
            if hand_count.get(color, 0) >= needed:
                hand_count[color] -= needed
                new_board = self.removeBalls(board[:i] + board[j:])
                
                steps = self.backtrack(new_board, hand_count)
                if steps != -1:
                    min_steps = min(min_steps, steps + needed)
                
                hand_count[color] += needed
            
            i = j
        
        return min_steps if min_steps != float('inf') else -1
    
    def removeBalls(self, board: str) -> str:
        i = 0
        while i < len(board):
            j = i
            while j < len(board) and board[j] == board[i]:
                j += 1
            if j - i >= 3:
                return self.removeBalls(board[:i] + board[j:])
            i = j
        return board