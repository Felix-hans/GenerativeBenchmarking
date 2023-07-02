# @lc app=leetcode id=715 lang=python3
class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_ranges = []
        i = 0
        n = len(self.ranges)

        while i < n and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < n and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            i += 1

        new_ranges.append((left, right))

        while i < n:
            new_ranges.append(self.ranges[i])
            i += 1

        self.ranges = new_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for range_left, range_right in self.ranges:
            if range_left <= left and range_right >= right:
                return True
            if range_left > left:
                break
        return False

    def removeRange(self, left: int, right: int) -> None:
        new_ranges = []
        i = 0
        n = len(self.ranges)

        while i < n and self.ranges[i][1] < left:
            new_ranges.append(self.ranges[i])
            i += 1

        while i < n and self.ranges[i][0] < right:
            if self.ranges[i][0] < left:
                new_ranges.append((self.ranges[i][0], left))
            if self.ranges[i][1] > right:
                new_ranges.append((right, self.ranges[i][1]))
            i += 1

        self.ranges = new_ranges