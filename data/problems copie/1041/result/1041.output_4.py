# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        x = 0
        y = 0
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for instruction in instructions:
            if instruction == 'G':
                x += dx[direction]
                y += dy[direction]
            elif instruction == 'L':
                direction = (direction - 1) % 4
            elif instruction == 'R':
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0