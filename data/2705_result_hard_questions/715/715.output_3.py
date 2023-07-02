# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        new_interval = [left, right]
        while i < len(self.intervals) and self.intervals[i][0] < right:
            new_interval[0] = min(new_interval[0], self.intervals[i][0])
            new_interval[1] = max(new_interval[1], self.intervals[i][1])
            del self.intervals[i]

        self.intervals.insert(i, tuple(new_interval))

    def queryRange(self, left: int, right: int) -> bool:
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
            elif interval[0] <= left < interval[1] or interval[0] < right <= interval[1]:
                return False
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                self.intervals.insert(i, (self.intervals[i][0], left))

            if self.intervals[i][1] > right:
                self.intervals.insert(i + 1, (right, self.intervals[i][1]))
                i += 2
            else:
                i += 1

            del self.intervals[i]

        self.intervals = [interval for interval in self.intervals if interval[0] != interval[1]]