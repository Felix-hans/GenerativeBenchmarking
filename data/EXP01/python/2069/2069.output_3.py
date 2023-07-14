# @lc app=leetcode id=2069 lang=python3
class Robot:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = "East"

    def step(self, num: int) -> None:
        for i in range(num):
            if self.direction == "North":
                if self.y + 1 >= self.height:
                    self.direction = "West"
                else:
                    self.y += 1
            elif self.direction == "East":
                if self.x + 1 >= self.width:
                    self.direction = "North"
                else:
                    self.x += 1
            elif self.direction == "South":
                if self.y - 1 < 0:
                    self.direction = "East"
                else:
                    self.y -= 1
            elif self.direction == "West":
                if self.x - 1 < 0:
                    self.direction = "South"
                else:
                    self.x -= 1

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction