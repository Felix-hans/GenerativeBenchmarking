# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        new_range = (left, right)
        merged_ranges = []
        for i, (start, end) in enumerate(self.ranges):
            if end < left:
                merged_ranges.append((start, end))
            elif right < start:
                merged_ranges.append(new_range)
                merged_ranges.extend(self.ranges[i:])
                break
            else:
                new_range = (min(start, left), max(end, right))
        else:
            merged_ranges.append(new_range)
        self.ranges = merged_ranges

    def queryRange(self, left: int, right: int) -> bool:
        for start, end in self.ranges:
            if left >= start and right <= end:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        removed_ranges = []
        for start, end in self.ranges:
            if end <= left or start >= right:
                removed_ranges.append((start, end))
            elif start < left and end > right:
                removed_ranges.append((start, left))
                removed_ranges.append((right, end))
            elif start < left:
                removed_ranges.append((start, left))
            elif end > right:
                removed_ranges.append((right, end))
        self.ranges = removed_ranges