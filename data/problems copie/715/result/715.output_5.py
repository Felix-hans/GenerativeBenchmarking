# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        merged = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] < left:
            merged.append(self.intervals[i])
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1

        merged.append((left, right))

        while i < len(self.intervals):
            merged.append(self.intervals[i])
            i += 1

        self.intervals = merged

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        if i < len(self.intervals) and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        merged = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] < left:
            merged.append(self.intervals[i])
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                merged.append((self.intervals[i][0], left))
            if self.intervals[i][1] > right:
                merged.append((right, self.intervals[i][1]))
            i += 1

        while i < len(self.intervals):
            merged.append(self.intervals[i])
            i += 1

        self.intervals = merged