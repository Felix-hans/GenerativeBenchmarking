# @lc app=leetcode id=2069 lang=python3
class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.direction = "East"
        
    def step(self, num: int) -> None:
        for _ in range(num):
            if self.direction == "North":
                self.y += 1
                if self.y >= self.height:
                    self.y -= 1
                    self.direction = "West"
            elif self.direction == "East":
                self.x += 1
                if self.x >= self.width:
                    self.x -= 1
                    self.direction = "North"
            elif self.direction == "South":
                self.y -= 1
                if self.y < 0:
                    self.y += 1
                    self.direction = "East"
            elif self.direction == "West":
                self.x -= 1
                if self.x < 0:
                    self.x += 1
                    self.direction = "South"
    
    def getPos(self) -> List[int]:
        return [self.x, self.y]
    
    def getDir(self) -> str:
        return self.direction