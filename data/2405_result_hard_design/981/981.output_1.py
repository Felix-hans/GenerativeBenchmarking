# @lc app=leetcode id=981 lang=python3
from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        timestamps = self.data[key]
        left, right = 0, len(timestamps) - 1

        while left <= right:
            mid = (left + right) // 2
            if timestamps[mid][0] == timestamp:
                return timestamps[mid][1]
            elif timestamps[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        if right >= 0:
            return timestamps[right][1]
        else:
            return ""