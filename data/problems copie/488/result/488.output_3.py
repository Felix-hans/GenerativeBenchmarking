# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def removeGroups(board):
            i, n = 0, len(board)
            while i < n:
                j = i
                while j < n and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    board = board[:i] + board[j:]
                    n = len(board)
                    i = max(0, i - 2)
                else:
                    i = j
            return board
        
        def dfs(board, hand):
            if not board:
                return 0  # Board is already empty
            
            if not hand:
                return -1  # No more balls to insert
            
            minBalls = float('inf')  # Initialize with a large value
            
            for i in range(len(hand)):
                for j in range(len(board) + 1):
                    newBoard = board[:j] + hand[i] + board[j:]
                    
                    newBoard = removeGroups(newBoard)
                    
                    res = dfs(newBoard, hand[:i] + hand[i+1:])
                    
                    if res != -1:
                        minBalls = min(minBalls, 1 + res)
            
            return minBalls if minBalls != float('inf') else -1

        handCount = Counter(hand)
        
        minBalls = dfs(board, handCount)
        
        return minBalls if minBalls != float('inf') else -1