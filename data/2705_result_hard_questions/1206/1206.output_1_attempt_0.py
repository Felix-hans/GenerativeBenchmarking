# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = []

class Skiplist:
    def __init__(self):
        self.head = Node(-float('inf'))
        self.tail = Node(float('inf'))
        self.head.next = [self.tail]

    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.next[0].value == target:
                return True
            elif node.next[0].value > target:
                node = node.next[0].down
            else:
                node = node.next[0]
        return False

    def add(self, num: int) -> None:
        node = self.head
        path = [node]

        while node:
            if node.next and node.next[0].value < num:
                node = node.next[0]
            else:
                path.append(node)
                node = node.down

        insert_node = Node(num)
        down = None

        for i in range(len(path) - 1, -1, -1):
            node = path[i]
            insert_node.next.append(node.next[i])
            node.next[i] = insert_node
            insert_node.down = down
            down = insert_node
            if random.random() < 0.5:
                break

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