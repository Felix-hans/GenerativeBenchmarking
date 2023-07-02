# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            self.intervals.pop(i)

        self.intervals.insert(i, (left, right))

    def queryRange(self, left: int, right: int) -> bool:
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.intervals) and self.intervals[i][1] <= left:
            i += 1

        while i < len(self.intervals) and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                self.intervals.append((self.intervals[i][0], left))
            if self.intervals[i][1] > right:
                self.intervals.append((right, self.intervals[i][1]))
            self.intervals.pop(i)

        self.intervals.sort()

rangeModule = RangeModule()
rangeModule.addRange(10, 20)
rangeModule.removeRange(14, 16)
print(rangeModule.queryRange(10, 14))  # Output: True
print(rangeModule.queryRange(13, 15))  # Output: False
print(rangeModule.queryRange(16, 17))  # Output: True