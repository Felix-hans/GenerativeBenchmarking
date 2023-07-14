# @lc app=leetcode id=295 lang=python3
import heapq

class MedianFinder:

    def __init__(self):
        self.small_heap = []  # max heap
        self.large_heap = []  # min heap

    def addNum(self, num: int) -> None:
        if not self.small_heap or num < -self.small_heap[0]:
            heapq.heappush(self.small_heap, -num)
        else:
            heapq.heappush(self.large_heap, num)

        if len(self.small_heap) - len(self.large_heap) > 1:
            heapq.heappush(self.large_heap, -heapq.heappop(self.small_heap))
        elif len(self.large_heap) - len(self.small_heap) > 1:
            heapq.heappush(self.small_heap, -heapq.heappop(self.large_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.large_heap):
            return (-self.small_heap[0] + self.large_heap[0]) / 2
        elif len(self.small_heap) > len(self.large_heap):
            return -self.small_heap[0]
        else:
            return self.large_heap[0]