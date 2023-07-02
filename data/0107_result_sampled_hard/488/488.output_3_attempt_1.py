# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def backtrack(board, hand):
            if not board:
                return 0

            min_steps = float('inf')
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1

                color = board[i]
                count = j - i
                needed = 3 - count

                if hand[color] >= needed:
                    hand[color] -= needed
                    new_board = removeConsecutive(board[:i] + board[j:])
                    steps = backtrack(new_board, hand.copy())  # Use a copy of hand counts
                    if steps >= 0:
                        min_steps = min(min_steps, needed + steps)
                    hand[color] += needed

                i = j

            return min_steps if min_steps != float('inf') else -1

        def removeConsecutive(board):
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    return removeConsecutive(board[:i] + board[j:])
                i = j
            return board

        board_count = Counter(board)
        hand_count = Counter(hand)
        return backtrack(board, hand_count)