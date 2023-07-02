# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] < right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            del self.ranges[i]

        self.ranges.insert(i, (left, right))

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] < left:
            i += 1

        if i < len(self.ranges) and self.ranges[i][0] <= left and self.ranges[i][1] >= right:
            return True

        return False

    def removeRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        while i < len(self.ranges) and self.ranges[i][0] < right:
            if self.ranges[i][0] < left:
                self.ranges.insert(i, (self.ranges[i][0], left))
                i += 1

            if self.ranges[i][1] > right:
                self.ranges.insert(i + 1, (right, self.ranges[i][1]))
                i += 2
            else:
                del self.ranges[i]

    def printRanges(self):
        for range in self.ranges:
            print(range)


rangeModule = RangeModule()
rangeModule.addRange(10, 180)
rangeModule.addRange(150, 200)
rangeModule.addRange(250, 500)
print(rangeModule.queryRange(50, 100))  # True
print(rangeModule.queryRange(180, 300))  # False
print(rangeModule.queryRange(600, 1000))  # False
rangeModule.removeRange(50, 150)
print(rangeModule.queryRange(50, 100))  # False
rangeModule.printRanges()