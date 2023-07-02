# @lc app=leetcode id=1206 lang=python3
import random

class ListNode:
    def __init__(self, val=None, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = ListNode()

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            while node.right and node.right.val < target:
                node = node.right
            if node.right and node.right.val == target:
                return True
            node = node.down
        return False

    def add(self, num: int) -> None:
        path = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            path.append(node)
            node = node.down

        insert = True
        down = None
        while insert and path:
            node = path.pop()
            node.right = ListNode(num, node.right, down)
            down = node.right
            insert = (random.getrandbits(1) == 0)  # 50% chance to stop inserting in the upper level

        if insert:
            self.head = ListNode(None, None, self.head)
            self.head.right = ListNode(num, None, down)

    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                node.right = node.right.right
                found = True
            node = node.down
        return found