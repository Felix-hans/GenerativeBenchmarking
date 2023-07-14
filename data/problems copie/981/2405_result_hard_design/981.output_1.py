# @lc app=leetcode id=981 lang=python3
import bisect

class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            values = self.data[key]
            index = bisect.bisect_right(values, (timestamp, chr(127)))
            if index > 0:
                return values[index - 1][1]
        return ""

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))   # Output: "bar"
print(timeMap.get("foo", 3))   # Output: "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))   # Output: "bar2"
print(timeMap.get("foo", 5))   # Output: "bar2"