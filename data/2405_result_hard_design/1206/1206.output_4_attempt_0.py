# @lc app=leetcode id=1206 lang=python3
import random

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = ListNode()
        self.levels = [self.head]

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            elif curr.right is None or curr.right.val > target:
                curr = curr.down
            else:
                curr = curr.right
        return False

    def add(self, num: int) -> None:
        nodes = []
        curr = self.head
        while curr:
            if curr.right is None or curr.right.val > num:
                nodes.append(curr)
                curr = curr.down
            else:
                curr = curr.right

        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            node.right = ListNode(num)
            node.right.down = down
            down = node.right
            insert = random.random() < 0.5  # 50% chance to go up one level

            if insert:
                new_node = ListNode()
                new_node.down = self.levels[-1]
                self.levels.append(new_node)
                node.right.right = new_node

    def erase(self, num: int) -> bool:
        found = False
        curr = self.head
        while curr:
            if curr.right is None or curr.right.val > num:
                curr = curr.down
            elif curr.right.val == num:
                found = True
                curr.right = curr.right.right
                curr = curr.down
            else:
                curr = curr.right
        return found