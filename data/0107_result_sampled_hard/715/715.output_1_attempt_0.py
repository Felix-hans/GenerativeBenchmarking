# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        start = left
        end = right
        while i < len(self.intervals) and self.intervals[i][0] <= right:
            start = min(start, self.intervals[i][0])
            end = max(end, self.intervals[i][1])
            del self.intervals[i]

        self.intervals.insert(i, (start, end))

    def queryRange(self, left: int, right: int) -> bool:
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        new_intervals = []
        for interval in self.intervals[:i]:
            new_intervals.append(interval)

        for interval in self.intervals[i:]:
            if interval[0] < left:
                new_intervals.append((interval[0], left))
            if interval[1] > right:
                new_intervals.append((right, interval[1]))

        self.intervals = new_intervals