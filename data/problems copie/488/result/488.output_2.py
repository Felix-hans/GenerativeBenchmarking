# @lc app=leetcode id=488 lang=python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_freq = {}
        for ball in hand:
            hand_freq[ball] = hand_freq.get(ball, 0) + 1

        def backtrack(board: str, hand_freq: dict) -> int:
            if not board:
                return 0  # Board is empty, game is won

            min_steps = float('inf')
            i = 0

            while i < len(board):
                j = i + 1

                while j < len(board) and board[j] == board[i]:
                    j += 1

                balls_needed = 3 - (j - i)

                if hand_freq.get(board[i], 0) >= balls_needed:
                    balls_removed = balls_needed if balls_needed > 0 else 0
                    hand_freq[board[i]] -= balls_removed

                    remaining_board = board[:i] + board[j:]
                    min_steps = min(min_steps, balls_removed + backtrack(remaining_board, hand_freq))

                    hand_freq[board[i]] += balls_removed

                i = j

            return min_steps

        min_steps = backtrack(board, hand_freq)

        return min_steps if min_steps != float('inf') else -1