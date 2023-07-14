# @lc app=leetcode id=767 lang=python3
from collections import Counter
from heapq import heappush, heappop

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        heap = []
        result = []

        for char, count in counts.items():
            heappush(heap, (-count, char))

        while len(heap) > 1:
            count1, char1 = heappop(heap)
            count2, char2 = heappop(heap)

            result.append(char1)
            result.append(char2)

            if count1 < -1:
                heappush(heap, (count1 + 1, char1))
            if count2 < -1:
                heappush(heap, (count2 + 1, char2))

        if heap:
            count, char = heappop(heap)
            if count < -1:
                return ""
            result.append(char)

        return "".join(result)