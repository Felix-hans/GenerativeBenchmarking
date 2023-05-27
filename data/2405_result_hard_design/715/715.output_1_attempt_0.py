# @lc app=leetcode id=715 lang=python3
class RangeModule:
    def __init__(self):
        self.intervals = []
    
    def addRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        
        while i < n and self.intervals[i][1] < left:
            new_intervals.append(self.intervals[i])
            i += 1
        
        while i < n and self.intervals[i][0] <= right:
            left = min(left, self.intervals[i][0])
            right = max(right, self.intervals[i][1])
            i += 1
        
        new_intervals.append((left, right))
        new_intervals.extend(self.intervals[i:])
        self.intervals = new_intervals
    
    def queryRange(self, left: int, right: int) -> bool:
        left_index = self.findInterval(left)
        
        if left_index == -1 or self.intervals[left_index][1] < right:
            return False
        
        return True
    
    def removeRange(self, left: int, right: int) -> None:
        new_intervals = []
        i = 0
        n = len(self.intervals)
        
        while i < n and self.intervals[i][1] <= left:
            new_intervals.append(self.intervals[i])
            i += 1
        
        while i < n and self.intervals[i][0] < right:
            if self.intervals[i][0] < left:
                new_intervals.append((self.intervals[i][0], left))
            if self.intervals[i][1] > right:
                new_intervals.append((right, self.intervals[i][1]))
            i += 1
        
        new_intervals.extend(self.intervals[i:])
        self.intervals = new_intervals
    
    def findInterval(self, point: int) -> int:
        left = 0
        right = len(self.intervals) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if self.intervals[mid][1] < point:
                left = mid + 1
            elif self.intervals[mid][0] > point:
                right = mid - 1
            else:
                return mid
        
        return right

rangeModule = RangeModule()
rangeModule.addRange(10, 20)
rangeModule.removeRange(14, 16)
print(rangeModule.queryRange(10, 14))  # Output: True
print(rangeModule.queryRange(13, 15))  # Output: False
print(rangeModule.queryRange(16, 17))  # Output: True