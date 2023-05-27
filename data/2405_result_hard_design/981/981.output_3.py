# @lc app=leetcode id=981 lang=python3
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
            left, right = 0, len(values) - 1

            while left <= right:
                mid = (left + right) // 2
                if values[mid][0] == timestamp:
                    return values[mid][1]
                elif values[mid][0] < timestamp:
                    left = mid + 1
                else:
                    right = mid - 1

            if right >= 0:
                return values[right][1]
        return ""

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))   # Output: "bar"
print(timeMap.get("foo", 3))   # Output: "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))   # Output: "bar2"
print(timeMap.get("foo", 5))   # Output: "bar2"