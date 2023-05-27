# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        if i > 0 and self.ranges[i-1][1] >= left:
            left = min(left, self.ranges[i-1][0])
            right = max(right, self.ranges[i-1][1])
            i -= 1

        while i < len(self.ranges) and self.ranges[i][0] <= right:
            left = min(left, self.ranges[i][0])
            right = max(right, self.ranges[i][1])
            self.ranges.pop(i)

        self.ranges.insert(i, (left, right))

    def queryRange(self, left: int, right: int) -> bool:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        if i < len(self.ranges) and self.ranges[i][0] <= left and self.ranges[i][1] >= right:
            return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        i = 0
        while i < len(self.ranges) and self.ranges[i][1] <= left:
            i += 1

        if i < len(self.ranges) and self.ranges[i][0] < left:
            self.ranges.insert(i, (self.ranges[i][0], left))

        j = i
        while j < len(self.ranges) and self.ranges[j][0] < right:
            if self.ranges[j][1] > right:
                self.ranges.insert(j+1, (right, self.ranges[j][1]))
                break
            else:
                self.ranges.pop(j)

    def printRanges(self):
        for r in self.ranges:
            print(f"[{r[0]}, {r[1]})")


rangeModule = RangeModule()
rangeModule.addRange(10, 20)
rangeModule.removeRange(14, 16)
print(rangeModule.queryRange(10, 14))  # True
print(rangeModule.queryRange(13, 15))  # False
print(rangeModule.queryRange(16, 17))  # True