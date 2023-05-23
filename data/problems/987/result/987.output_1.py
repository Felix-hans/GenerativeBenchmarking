# @lc app=leetcode id=987 lang=python3
from typing import List, Optional
from collections import defaultdict
from heapq import heappush, heappop
from TreeNode import TreeNode  # Assuming the TreeNode class is available

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)

        def dfs(node, row, col):
            if node:
                heappush(columns[col], (row, node.val))

                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)

        dfs(root, 0, 0)

        result = []
        for col in sorted(columns):
            column_nodes = []
            while columns[col]:
                column_nodes.append(heappop(columns[col])[1])  # Get the node value
            result.append(column_nodes)

        return result