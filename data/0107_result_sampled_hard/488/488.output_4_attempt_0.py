# @lc app=leetcode id=488 lang=python3
from collections import Counter

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_count = Counter(hand)

        def backtrack(board, hand_count):
            if not board:
                return 0

            min_balls = float('inf')

            i = 0
            while i < len(board):
                ball = board[i]
                color = ball

                j = i + 1
                while j < len(board) and board[j] == ball:
                    color += ball
                    j += 1

                if j - i >= 3 and hand_count[color] >= 3 - (j - i):
                    new_board = board[:i] + board[j:]

                    hand_count[color] -= 3 - (j - i)

                    balls = backtrack(new_board, hand_count)

                    if balls >= 0:
                        min_balls = min(min_balls, balls + 3 - (j - i))

                    hand_count[color] += 3 - (j - i)

                    i = j
                else:
                    i += 1

            return min_balls if min_balls != float('inf') else -1

        return backtrack(board, hand_count)