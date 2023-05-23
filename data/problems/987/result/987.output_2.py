# @lc app=leetcode id=987 lang=python3
from typing import List, Optional
from collections import defaultdict
from heapq import heappush, heappop

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)

        def dfs(node, row, col):
            if node is None:
                return

            heappush(columns[col], (row, node.val))

            dfs(node.left, row + 1, col - 1)
            dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(columns.keys()):
            column_nodes = []
            while columns[col]:
                column_nodes.append(heappop(columns[col])[1])
            result.append(column_nodes)

        return result