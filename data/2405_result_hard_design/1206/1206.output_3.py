# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node()
        self.max_level = 16  # Maximum number of levels in the skiplist
        self.level = 0  # Current level of the skiplist

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            elif curr.next and curr.next.val <= target:
                curr = curr.next
            else:
                curr = curr.down
        return False

    def add(self, num: int) -> None:
        level = 0
        curr = self.head
        stack = []  # Track the nodes at each level where insertion should occur
        while curr:
            if curr.next and curr.next.val < num:
                curr = curr.next
            else:
                stack.append(curr)
                curr = curr.down
                level += 1
                if level > self.level:  # Create a new level if needed
                    stack.append(self.head)
                    self.level += 1

        insert = True
        down = None
        while insert and stack:
            curr = stack.pop()
            new_node = Node(num)
            new_node.down = down
            down = new_node
            new_node.next = curr.next
            curr.next = new_node
            insert = random.choice([True, False])  # Randomly decide whether to insert at the upper level

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.next and curr.next.val < num:
                curr = curr.next
            elif curr.next and curr.next.val == num:
                curr.next = curr.next.next
                curr = curr.down
                found = True
            else:
                curr = curr.down
        return found