# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.next = self.tail
        self.levels = [self.head]  # Stores the nodes at the highest level

    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.next.val == target:
                return True
            elif curr.next.val > target:
                curr = curr.down
            else:
                curr = curr.next
        return False

    def add(self, num: int) -> None:
        nodes = []  # Stores the nodes where the new value is inserted
        curr = self.head
        while curr:
            if curr.next.val == num:
                nodes.append(curr.next)
                curr = curr.down
            elif curr.next.val > num:
                nodes.append(curr)
                curr = curr.down
            else:
                curr = curr.next

        down_node = None
        insert_up = True  # Determines whether to insert a node at the upper level
        for node in reversed(nodes):
            new_node = Node(num)
            new_node.next = node.next
            node.next = new_node
            if down_node:
                new_node.down = down_node
            down_node = new_node

            if insert_up:
                coin = random.randint(0, 1)
                if coin == 1:
                    new_level = Node(float('-inf'))
                    new_level.next = new_node
                    new_level.down = self.levels[-1]
                    self.levels.append(new_level)
                    insert_up = False

    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.next.val == num:
                found = True
                curr.next = curr.next.next
                curr = curr.down
            elif curr.next.val > num:
                curr = curr.down
            else:
                curr = curr.next
        return found