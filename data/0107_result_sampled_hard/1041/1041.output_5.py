# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0  # Position
        dx, dy = 0, 1  # Direction (north)

        for _ in range(4):
            for instruction in instructions:
                if instruction == 'G':
                    x += dx
                    y += dy
                elif instruction == 'L':
                    dx, dy = -dy, dx  # Rotate 90 degrees to the left
                elif instruction == 'R':
                    dx, dy = dy, -dx  # Rotate 90 degrees to the right

        return x == 0 and y == 0