# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))  # Head node with negative infinity value
        self.levels = [self.head]  # List to store the head nodes of each level
    
    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.val == target:
                return True
            elif node.right is None or node.right.val > target:
                node = node.down
            else:
                node = node.right
        return False
    
    def add(self, num: int) -> None:
        path = self._get_path(num)
        down = None
        for node in reversed(path):
            new_node = Node(num)
            new_node.right = node.right
            node.right = new_node
            new_node.down = down
            down = new_node
            if random.random() < 0.5:
                break
    
    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            if node.right is None or node.right.val > num:
                node = node.down
            elif node.right.val == num:
                node.right = node.right.right
                found = True
                node = node.down
            else:
                node = node.right
        return found
    
    def _get_path(self, num: int) -> list:
        node = self.head
        path = []
        while node:
            if node.right is None or node.right.val > num:
                path.append(node)
                node = node.down
            elif node.right.val == num:
                path.append(node)
                return path
            else:
                node = node.right
        return path