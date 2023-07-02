# @lc app=leetcode id=1483 lang=python3
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.MAX_DEPTH = 16  # Maximum depth for efficient precomputation
        self.n = n
        self.ancestors = [[-1] * self.MAX_DEPTH for _ in range(n)]

        for i in range(n):
            self.ancestors[i][0] = parent[i]

        for j in range(1, self.MAX_DEPTH):
            for i in range(n):
                if self.ancestors[i][j - 1] != -1:
                    self.ancestors[i][j] = self.ancestors[self.ancestors[i][j - 1]][j - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        if node < 0 or node >= self.n:
            return -1

        for i in range(self.MAX_DEPTH - 1, -1, -1):
            if k >= (1 << i):
                node = self.ancestors[node][i]
                if node == -1:
                    return -1
                k -= (1 << i)

        return node