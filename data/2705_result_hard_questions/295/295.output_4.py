# @lc app=leetcode id=295 lang=python3
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []  # stores the larger half of the numbers
        self.max_heap = []  # stores the smaller half of the numbers
        
    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -num)
            
            max_num = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, max_num)
        else:
            heapq.heappush(self.min_heap, num)
            
            min_num = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_num)
            
    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return float(self.min_heap[0])