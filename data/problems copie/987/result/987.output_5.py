# @lc app=leetcode id=987 lang=python3
from typing import List, Optional
from collections import defaultdict
from heapq import heappop, heappush

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_map = defaultdict(list)

        def dfs(node, row, col):
            if node:
                heappush(column_map[col], (row, node.val))

                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(column_map):
            column_values = []
            while column_map[col]:
                column_values.append(heappop(column_map[col])[1])
            result.append(column_values)

        return result