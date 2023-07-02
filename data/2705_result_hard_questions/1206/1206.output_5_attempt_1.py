# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.right = self.tail
        self.levels = [self.head]  # List to keep track of the levels

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            elif curr.right.val > target:
                curr = curr.down
            else:
                curr = curr.right
        return False

    def add(self, num: int) -> None:
        curr = self.head
        stack = []  # Stack to keep track of the levels where the new node is inserted
        while curr:
            if curr.right.val > num:
                stack.append(curr)
                curr = curr.down
            else:
                curr = curr.right

        down = None
        insert = True
        while insert and stack:
            curr = stack.pop()
            node = Node(num)
            node.down = down
            down = node
            node.right = curr.right
            curr.right = node
            insert = random.random() < 0.5  # Randomly decide whether to insert at the next level

            if insert:
                new_head = Node(float('-inf'))
                new_tail = Node(float('inf'))
                new_head.right = new_tail
                new_head.down = self.head
                new_tail.down = self.tail
                new_tail.right = self.tail
                self.head = new_head
                self.tail = new_tail
                self.head.right = self.tail
                self.head.down = down
                down = self.head
                self.levels.append(self.head)

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.right.val == num:
                curr.right = curr.right.right
                curr = curr.down
                found = True
            elif curr.right.val > num:
                curr = curr.down
            else:
                curr = curr.right
        return found