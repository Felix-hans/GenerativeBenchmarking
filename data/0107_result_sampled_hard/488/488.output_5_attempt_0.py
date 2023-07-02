# @lc app=leetcode id=488 lang=python3
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def removeConsecutiveBalls(board):
            stack = []
            i = 0
            while i < len(board):
                if not stack or stack[-1][0] != board[i]:
                    stack.append((board[i], 1))
                else:
                    stack[-1] = (stack[-1][0], stack[-1][1] + 1)
                    if stack[-1][1] >= 3:
                        stack.pop()
                i += 1
            return ''.join(ball[0] * ball[1] for ball in stack)

        def backtrack(board, hand):
            if not board:
                return 0

            min_balls = float('inf')
            i = 0
            while i < len(board):
                ball = board[i]
                count = hand.get(ball, 0)
                if count > 0:
                    hand[ball] -= 1
                    new_board = removeConsecutiveBalls(board[:i] + ball + board[i:])
                    balls_needed = backtrack(new_board, hand)
                    if balls_needed >= 0:
                        min_balls = min(min_balls, 1 + balls_needed)
                    hand[ball] += 1
                    i += 1
                else:
                    i += 1
            return min_balls if min_balls != float('inf') else -1

        hand_dict = {}
        for ball in hand:
            hand_dict[ball] = hand_dict.get(ball, 0) + 1

        return backtrack(board, hand_dict)