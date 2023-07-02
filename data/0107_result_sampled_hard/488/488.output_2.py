# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def backtrack(board, hand):
            if not board:
                return 0  # Board is empty, game is won

            min_steps = float('inf')  # Initialize with a large value

            i = 0
            while i < len(board):
                j = i
                while j < len(board) and board[j] == board[i]:
                    j += 1

                needed_balls = 3 - (j - i)
                if hand[board[i]] >= needed_balls:
                    removed_balls = j - i
                    new_board = board[:i] + board[j:]

                    steps = backtrack(new_board, hand)

                    if steps >= 0:
                        hand[board[i]] -= needed_balls
                        min_steps = min(min_steps, steps + needed_balls)

                    hand[board[i]] += needed_balls

                i = j

            if min_steps == float('inf'):
                return -1  # Cannot remove any more balls

            return min_steps

        board_count = Counter(board)
        hand_count = Counter(hand)
        return backtrack(board, hand_count)