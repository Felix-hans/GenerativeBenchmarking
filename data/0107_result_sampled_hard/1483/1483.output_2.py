# @lc app=leetcode id=1483 lang=python3
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.ancestors = [[-1] * int(math.log2(n) + 1) for _ in range(n)]
        
        for node in range(n):
            self.ancestors[node][0] = parent[node]

        for k in range(1, int(math.log2(n)) + 1):
            for node in range(n):
                if self.ancestors[node][k - 1] != -1:
                    self.ancestors[node][k] = self.ancestors[self.ancestors[node][k - 1]][k - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(int(math.log2(len(self.ancestors[node]))), -1, -1):
            if node == -1 or k == 0:
                break
            if k >= (1 << i):
                node = self.ancestors[node][i]
                k -= 1 << i
        return node