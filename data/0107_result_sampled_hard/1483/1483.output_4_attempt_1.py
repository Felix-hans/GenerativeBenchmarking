# @lc app=leetcode id=1483 lang=python3
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.max_depth = 16  # Maximum depth for preprocessing (can be adjusted)
        self.dp = [[-1] * self.max_depth for _ in range(n)]  # Ancestor lookup table

        for node in range(n):
            self.dp[node][0] = parent[node]  # 2^0th ancestor is the immediate parent

            for depth in range(1, self.max_depth):
                if self.dp[node][depth - 1] != -1:
                    self.dp[node][depth] = self.dp[self.dp[node][depth - 1]][depth - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for depth in range(self.max_depth - 1, -1, -1):
            if k & (1 << depth):
                node = self.dp[node][depth]
                if node == -1:
                    break

        return node

treeAncestor = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
print(treeAncestor.getKthAncestor(3, 1))  # Output: 1
print(treeAncestor.getKthAncestor(5, 2))  # Output: 0
print(treeAncestor.getKthAncestor(6, 3))  # Output: -1