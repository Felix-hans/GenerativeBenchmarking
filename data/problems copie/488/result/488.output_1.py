# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        self.min_balls = float('inf')
        hand_count = Counter(hand)
        self.backtrack(board, hand_count)
        return self.min_balls if self.min_balls < float('inf') else -1

    def backtrack(self, board, hand_count, balls_used=0):
        if not board:
            self.min_balls = min(self.min_balls, balls_used)
            return

        if not hand_count:
            return

        i = 0
        while i < len(board):
            j = i + 1
            while j < len(board) and board[i] == board[j]:
                j += 1

            needed_balls = 3 - (j - i)
            if hand_count[board[i]] >= needed_balls:
                removed_balls = board[i:j]
                new_board = self.remove_balls(board[:i] + board[j:])
                hand_count[board[i]] -= needed_balls
                self.backtrack(new_board, hand_count, balls_used + needed_balls)
                hand_count[board[i]] += needed_balls

            i = j

    def remove_balls(self, board):
        i = 0
        while i < len(board):
            j = i + 1
            while j < len(board) and board[i] == board[j]:
                j += 1

            if j - i >= 3:
                return self.remove_balls(board[:i] + board[j:])

            i = j

        return board