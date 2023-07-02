# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, value=None, level=0):
        self.value = value
        self.next = []
        self.down = None
        self.level = level

class Skiplist:
    def __init__(self):
        self.head = Node(-float('inf'))
        self.tail = Node(float('inf'))
        self.head.next = [self.tail]
        self.levels = 1

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.next[0].value == target:
                return True
            elif node.next[0].value > target:
                node = node.down
            else:
                node = node.next[0]
        return False

    def add(self, num: int) -> None:
        node = self.head
        path = [None] * self.levels

        while node:
            if node.next and node.next[0].value < num:
                node = node.next[0]
            else:
                path[node.level] = node
                node = node.down

        insert_node = Node(num)
        level = 0
        down = None

        while random.random() < 0.5:
            if level >= self.levels:
                self.levels += 1
                self.head.next.append(self.tail)
                path.append(None)

            if level >= len(path):
                path.append(self.head)

            node = Node(num, level)
            node.down = down
            down = node

            prev = path[level]
            node.next.append(prev.next[level])
            prev.next[level] = node

            level += 1

    def erase(self, num: int) -> bool:
        node = self.head
        found = False

        while node:
            if node.next and node.next[0].value < num:
                node = node.next[0]
            else:
                if node.next[0].value == num:
                    found = True
                node.next[0] = node.next[0].next[0]
                node = node.down

        return found