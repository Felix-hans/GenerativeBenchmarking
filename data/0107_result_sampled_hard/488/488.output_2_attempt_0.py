# @lc app=leetcode id=488 lang=python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_count = {}
        for ball in hand:
            hand_count[ball] = hand_count.get(ball, 0) + 1

        def removeBalls(board):
            if not board:
                return 0  # Board is empty, game is won

            min_steps = float('inf')  # Initialize with a large value

            i = 0
            while i < len(board):
                j = i + 1
                while j < len(board) and board[j] == board[i]:
                    j += 1

                needed_balls = 3 - (j - i)
                if hand_count.get(board[i], 0) >= needed_balls:
                    removed_balls = j - i
                    new_board = board[:i] + board[j:]
                    removed_ball = board[i]
                    while i < len(new_board) and new_board[i] == removed_ball:
                        i += 1

                    steps = removeBalls(new_board)

                    if steps >= 0:
                        hand_count[removed_ball] -= needed_balls
                        min_steps = min(min_steps, steps + needed_balls)

                    hand_count[removed_ball] += needed_balls

                i = j

            if min_steps == float('inf'):
                return -1  # Cannot remove any more balls

            return min_steps

        return removeBalls(board)