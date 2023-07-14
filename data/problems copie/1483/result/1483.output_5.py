# @lc app=leetcode id=1483 lang=python3
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.max_level = 17  # Assuming the maximum number of nodes is 2^17
        self.dp = [[-1] * self.max_level for _ in range(n)]  # Initialize dp table

        for node in range(n):
            self.dp[node][0] = parent[node]

        for level in range(1, self.max_level):
            for node in range(n):
                if self.dp[node][level - 1] != -1:
                    parent_node = self.dp[node][level - 1]
                    self.dp[node][level] = self.dp[parent_node][level - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for level in range(self.max_level - 1, -1, -1):
            if node == -1 or k == 0:
                break

            if k >= (1 << level):
                node = self.dp[node][level]
                k -= 1 << level

        return node