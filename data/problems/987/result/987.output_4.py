# @lc app=leetcode id=987 lang=python3
from typing import List, Optional
from collections import defaultdict
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        column_nodes = defaultdict(list)

        queue = Queue()
        col_queue = Queue()

        queue.put(root)
        col_queue.put(0)

        while not queue.empty():
            node = queue.get()
            col_index = col_queue.get()

            column_nodes[col_index].append(node.val)

            if node.left:
                queue.put(node.left)
                col_queue.put(col_index - 1)

            if node.right:
                queue.put(node.right)
                col_queue.put(col_index + 1)

        vertical_order = []
        for col_index in sorted(column_nodes.keys()):
            column = column_nodes[col_index]
            column.sort()
            vertical_order.append(column)

        return vertical_order