# @lc app=leetcode id=987 lang=python3
from typing import List, Optional
from collections import defaultdict
from queue import Queue
from itertools import groupby

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        columns = defaultdict(list)
        queue = Queue()
        queue.put((root, 0))

        while not queue.empty():
            size = queue.qsize()
            column_nodes = defaultdict(list)

            for _ in range(size):
                node, col = queue.get()

                column_nodes[col].append(node.val)

                if node.left:
                    queue.put((node.left, col - 1))

                if node.right:
                    queue.put((node.right, col + 1))

            for col, nodes in column_nodes.items():
                columns[col].extend(sorted(nodes))

        sorted_columns = sorted(columns.items(), key=lambda x: x[0])

        vertical_traversal = [nodes for _, nodes in sorted_columns]

        return vertical_traversal