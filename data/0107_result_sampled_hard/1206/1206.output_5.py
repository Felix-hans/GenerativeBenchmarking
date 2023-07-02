# @lc app=leetcode id=1206 lang=python3
import random

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = ListNode(float('-inf'))
        self.tail = ListNode(float('inf'))
        self.head.right = self.tail
        self.max_level = 1
        
    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.val == target:
                return True
            elif node.right and node.right.val <= target:
                node = node.right
            else:
                node = node.down
        return False

    def add(self, num: int) -> None:
        level = 1
        while random.random() < 0.5:
            level += 1
        if level > self.max_level:
            self.insert_level()
            self.max_level = level
        node = self.head
        new_node = ListNode(num)
        path = []
        for i in range(self.max_level):
            while node.right and node.right.val < num:
                node = node.right
            path.append(node)
            node = node.down
        insert_node = None  # Initialize insert_node to None
        for i in range(level):
            insert_node = ListNode(num)
            insert_node.right = path.pop().right if path else self.tail  # Handle empty path list
            if path:
                path[-1].right = insert_node
            insert_node.down = new_node
            new_node = insert_node
        if path:
            path[-1].right = insert_node

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            if node.right and node.right.val < num:
                node = node.right
            elif node.right and node.right.val == num:
                node.right = node.right.right
                found = True
                node = node.down
            else:
                node = node.down
        return found
    
    def insert_level(self):
        new_head = ListNode(float('-inf'))
        new_head.right = self.tail
        new_head.down = self.head
        self.head = new_head