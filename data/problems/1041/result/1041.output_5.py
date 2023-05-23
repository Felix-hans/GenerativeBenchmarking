# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0  # coordinates
        dx, dy = 0, 1  # direction (north)

        for instruction in instructions:
            if instruction == 'G':
                x += dx
                y += dy
            elif instruction == 'L':
                dx, dy = -dy, dx
            elif instruction == 'R':
                dx, dy = dy, -dx

        return (x == 0 and y == 0) or (dx != 0 or dy != 1)