# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.levels = 1

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            elif curr.next.val > target:
                curr = curr.down
            else:
                curr = curr.next
        return False

    def add(self, num: int) -> None:
        nodes = []
        curr = self.head
        while curr:
            if curr.next.val > num:
                nodes.append(curr)
                curr = curr.down
            else:
                curr = curr.next

        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            new_node = Node(num)
            new_node.next = node.next
            node.next = new_node
            new_node.down = down
            down = new_node
            insert = random.random() < 0.5

            if insert:
                if self.levels == node.next:
                    self.levels += 1

        if insert:
            new_node = Node(num)
            new_node.next = self.tail
            new_node.down = down
            self.head = Node(float('-inf'))
            self.head.next = new_node
            self.head.down = self.head

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.next.val == num:
                curr.next = curr.next.next
                curr = curr.down
                found = True
            elif curr.next.val > num:
                curr = curr.down
            else:
                curr = curr.next
        return found