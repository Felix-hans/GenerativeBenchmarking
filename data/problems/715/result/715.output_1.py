# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1

        new_ranges.append((left, right))
        new_ranges.extend(self.ranges[i:])
        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        if i == len(self.ranges) or self.ranges[i][0] > right:
            return False

        return True

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] < right:
            if self.ranges[i][0] < left:
                new_ranges.append((self.ranges[i][0], left))
            if self.ranges[i][1] > right:
                new_ranges.append((right, self.ranges[i][1]))
            i += 1

        new_ranges.extend(self.ranges[i:])
        self.ranges = new_ranges