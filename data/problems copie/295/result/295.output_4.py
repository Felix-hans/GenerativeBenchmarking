# @lc app=leetcode id=295 lang=python3
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []  # stores the larger half of the numbers
        self.max_heap = []  # stores the smaller half of the numbers

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if self.min_heap and -self.max_heap[0] > self.min_heap[0]:
            max_heap_top = -heapq.heappop(self.max_heap)
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_heap_top)
            heapq.heappush(self.min_heap, max_heap_top)

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]