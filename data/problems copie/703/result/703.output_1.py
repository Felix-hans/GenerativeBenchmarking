# @lc app=leetcode id=703 lang=python3
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []
        
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

kthLargest = KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3))   # Output: 4
print(kthLargest.add(5))   # Output: 5
print(kthLargest.add(10))  # Output: 5
print(kthLargest.add(9))   # Output: 8
print(kthLargest.add(4))   # Output: 8