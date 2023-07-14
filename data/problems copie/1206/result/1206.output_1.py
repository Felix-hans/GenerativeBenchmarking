# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = Node()  # Dummy node at the top-left corner

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.right is None or curr.right.val > target:
                curr = curr.down
            elif curr.right.val == target:
                return True
            else:
                curr = curr.right
        return False

    def add(self, num: int) -> None:
        stack = []
        curr = self.head
        while curr:
            if curr.right is None or curr.right.val > num:
                stack.append(curr)  # Store the node before potential insertion point
                curr = curr.down
            elif curr.right.val == num:
                new_node = Node(num, curr.right, None)
                curr.right = new_node
                curr = curr.down
            else:
                curr = curr.right

        level = 0  # Current level
        insert_up = True  # Flag to determine whether to insert a new level
        while insert_up and stack:
            prev = stack.pop()
            prev.right = Node(num, prev.right, None)
            prev.right.down = curr
            curr = prev.right
            insert_up = random.choice([True, False])  # Randomly decide whether to insert a new level
            if insert_up:
                new_node = Node(None, None, curr)
                curr = new_node
                if level == 0:
                    self.head = new_node
                level += 1

    def erase(self, num: int) -> bool:
        found = False
        curr = self.head
        while curr:
            if curr.right is None or curr.right.val > num:
                curr = curr.down
            elif curr.right.val == num:
                curr.right = curr.right.right
                curr = curr.down
                found = True
            else:
                curr = curr.right
        return found