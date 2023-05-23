# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        dx, dy = 0, 1  # North direction

        for i in instructions:
            if i == 'G':
                x += dx
                y += dy
            elif i == 'L':
                dx, dy = -dy, dx  # Rotate 90 degrees counter-clockwise
            elif i == 'R':
                dx, dy = dy, -dx  # Rotate 90 degrees clockwise

        return (x, y) == (0, 0) or (dx, dy) != (0, 1)