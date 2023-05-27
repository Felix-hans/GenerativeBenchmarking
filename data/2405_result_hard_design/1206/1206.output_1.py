# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node()  # Dummy head node

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.right and curr.right.val < target:
                curr = curr.right
            elif curr.right and curr.right.val == target:
                return True
            else:
                curr = curr.down
        return False

    def add(self, num: int) -> None:
        stack = []
        curr = self.head
        while curr:
            if curr.right and curr.right.val < num:
                curr = curr.right
            elif curr.right and curr.right.val == num:
                curr.right.val = num  # Handle duplicates
                return
            else:
                stack.append(curr)
                curr = curr.down

        insert = True
        down = None
        while insert and stack:
            node = stack.pop()
            node.right = Node(num)
            node.right.down = down
            down = node.right
            insert = random.random() < 0.5

        if insert:
            self.head = Node()
            self.head.right = Node(num)
            self.head.down = down

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.right and curr.right.val < num:
                curr = curr.right
            elif curr.right and curr.right.val == num:
                curr.right = curr.right.right
                found = True
                curr = curr.down
            else:
                curr = curr.down
        return found