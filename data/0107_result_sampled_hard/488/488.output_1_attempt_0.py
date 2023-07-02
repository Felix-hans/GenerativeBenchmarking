# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def remove_groups(board):
            i, n = 0, len(board)
            while i < n:
                j = i
                while j < n and board[j] == board[i]:
                    j += 1
                if j - i >= 3:
                    return remove_groups(board[:i] + board[j:])
                i = j
            return board

        def backtrack(board, hand):
            if not board:
                return 0

            min_steps = float('inf')
            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1

                needed_balls = 3 - (j - i)
                if needed_balls <= len(hand.get(board[i], '')):
                    used_balls = max(0, needed_balls)
                    remaining_board = board[:i] + board[j:]
                    new_board = remove_groups(remaining_board)
                    remaining_hand = hand.copy()
                    for k in range(i, j):
                        if needed_balls > 0 and board[i] in remaining_hand:
                            remaining_hand[board[i]] -= 1
                            needed_balls -= 1
                    min_steps = min(min_steps, used_balls + backtrack(new_board, remaining_hand))

                i = j

            return min_steps

        board_counter = Counter(board)
        hand_counter = Counter(hand)
        return backtrack(board, hand_counter) if hand_counter else -1