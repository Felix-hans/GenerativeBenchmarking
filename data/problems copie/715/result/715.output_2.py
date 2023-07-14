# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []
        
    def addRange(self, left: int, right: int) -> None:
        new_range = (left, right)
        merged = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            merged.append(self.ranges[i])
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] <= right:
            new_range = (min(new_range[0], self.ranges[i][0]), max(new_range[1], self.ranges[i][1]))
            i += 1

        merged.append(new_range)

        while i < len(self.ranges):
            merged.append(self.ranges[i])
            i += 1

        self.ranges = merged

    def queryRange(self, left: int, right: int) -> bool:
        for range in self.ranges:
            if range[0] <= left and range[1] >= right:
                return True
            elif range[0] > left:
                return False
        return False

    def removeRange(self, left: int, right: int) -> None:
        merged = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            merged.append(self.ranges[i])
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] < right:
            if self.ranges[i][0] < left:
                merged.append((self.ranges[i][0], left))
            if self.ranges[i][1] > right:
                merged.append((right, self.ranges[i][1]))
            i += 1

        while i < len(self.ranges):
            merged.append(self.ranges[i])
            i += 1

        self.ranges = merged