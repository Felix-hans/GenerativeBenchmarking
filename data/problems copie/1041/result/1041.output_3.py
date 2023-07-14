# @lc app=leetcode id=1041 lang=python3
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0  # 0: north, 1: east, 2: south, 3: west
        x, y = 0, 0

        for instruction in instructions:
            if instruction == "G":
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                else:  # direction == 3
                    x -= 1
            elif instruction == "L":
                direction = (direction - 1) % 4
            elif instruction == "R":
                direction = (direction + 1) % 4

        return (x == 0 and y == 0) or direction != 0