# @lc app=leetcode id=295 lang=python3
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)

        max_heap_max = -heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_max)

        if len(self.max_heap) < len(self.min_heap):
            min_heap_min = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_min)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        else:
            return -self.max_heap[0]