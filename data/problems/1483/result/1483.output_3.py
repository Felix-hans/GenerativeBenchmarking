# @lc app=leetcode id=1483 lang=python3
from typing import List

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.max_depth = 16  # Assuming the maximum number of nodes is 2^16 = 65536
        self.dp = [[-1] * self.max_depth for _ in range(n)]  # Initialize the dp table

        for node in range(n):
            self.dp[node][0] = parent[node]  # The 1st ancestor is the parent itself
            for depth in range(1, self.max_depth):
                if self.dp[node][depth-1] != -1:
                    parent_of_parent = self.dp[node][depth-1]
                    self.dp[node][depth] = self.dp[parent_of_parent][depth-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for depth in range(self.max_depth):
            if k & (1 << depth):
                if node == -1:
                    return -1
                node = self.dp[node][depth]

        return node