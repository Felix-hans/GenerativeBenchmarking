# @lc app=leetcode id=981 lang=python3
from collections import defaultdict
from bisect import bisect_right

class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        values = self.data[key]
        index = bisect_right(values, (timestamp, chr(127)))

        if index == 0:
            return ""

        return values[index - 1][1]