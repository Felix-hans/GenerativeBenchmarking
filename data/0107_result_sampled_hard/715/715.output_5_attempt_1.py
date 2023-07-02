# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            del self.ranges[i]

        self.ranges.insert(i, (left, right))

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        if i < len(self.ranges) and self.ranges[i][0] <= left:
            return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        i, j = 0, len(self.ranges) - 1
        while i < len(self.ranges) and self.ranges[i][1] < left:
            i += 1
        while j >= 0 and self.ranges[j][0] > right:
            j -= 1

        del self.ranges[i:j+1]

        if i < len(self.ranges) and self.ranges[i][0] < left:
            self.ranges.insert(i, (self.ranges[i][0], left))
            i += 1
        if j >= 0 and self.ranges and self.ranges[j][1] > right:
            self.ranges.insert(i, (right, self.ranges[j][1]))

rangeModule = RangeModule()
rangeModule.addRange(10, 20)
rangeModule.removeRange(14, 16)
print(rangeModule.queryRange(10, 14))  # Output: True
print(rangeModule.queryRange(13, 15))  # Output: False
print(rangeModule.queryRange(16, 17))  # Output: True