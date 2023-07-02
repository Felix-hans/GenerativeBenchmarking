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
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        for interval in self.intervals:
            if interval[1] <= left or interval[0] >= right:
                new_intervals.append(interval)
            else:
                if interval[0] < left:
                    new_intervals.append((interval[0], left))
                if interval[1] > right:
                    new_intervals.append((right, interval[1]))

        self.intervals = new_intervals

rangeModule = RangeModule()
rangeModule.addRange(10, 20)
rangeModule.removeRange(14, 16)
print(rangeModule.queryRange(10, 14))  # Output: True
print(rangeModule.queryRange(13, 15))  # Output: False
print(rangeModule.queryRange(16, 17))  # Output: True