# @lc app=leetcode id=488 lang=python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def removeConsecutive(board):
            i, j = 0, 0
            while j < len(board):
                if board[i] == board[j]:
                    j += 1
                elif j - i >= 3:
                    return removeConsecutive(board[:i] + board[j:])
                else:
                    i = j
            return board
        
        def backtrack(board, hand):
            if not board:
                return 0  # Board is empty, we have won

            if not hand:
                return -1  # No more balls to insert from the hand

            min_steps = float('inf')
            i = 0

            while i < len(board):
                ball = board[i]
                j = i + 1

                while j < len(board) and board[j] == ball:
                    j += 1

                count = j - i  # Number of consecutive balls of the same color
                needed_balls = 3 - count  # Number of balls needed to remove the group

                if hand.count(ball) >= needed_balls:
                    new_board = removeConsecutive(board[:i] + board[j:])
                    remaining_hand = hand.replace(ball * needed_balls, '', needed_balls)
                    result = backtrack(new_board, remaining_hand)
                    if result != -1:
                        min_steps = min(min_steps, needed_balls + result)

                i = j

            if min_steps == float('inf'):
                return -1  # Cannot clear the board from this state
            else:
                return min_steps

        return backtrack(board, hand)