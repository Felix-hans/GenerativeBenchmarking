# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1

        new_intervals.append((left, right))
        new_intervals.extend(self.intervals[i:])
        self.intervals = new_intervals

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        if i < len(self.intervals) and self.intervals[i][0] <= left and self.intervals[i][1] >= right:
            return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            new_intervals.append(self.intervals[i])
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                new_intervals.append((self.intervals[i][0], left))
            if self.intervals[i][1] > right:
                new_intervals.append((right, self.intervals[i][1]))
            i += 1

        new_intervals.extend(self.intervals[i:])
        self.intervals = new_intervals