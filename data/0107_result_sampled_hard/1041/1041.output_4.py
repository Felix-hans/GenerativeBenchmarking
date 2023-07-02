# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for instruction in instructions:
            if instruction == 'G':
                dx, dy = directions[direction]
                x += dx
                y += dy
            elif instruction == 'L':
                direction = (direction - 1) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0