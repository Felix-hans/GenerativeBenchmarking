# @lc app=leetcode id=1206 lang=python3
import random

class SkipNode:
    def __init__(self, value=None, level=0):
        self.value = value
        self.forward = [None] * (level + 1)
        self.backward = None

class Skiplist:
    def __init__(self):
        self.max_level = 16  # Maximum level of the SkipList
        self.head = SkipNode()  # Head node with the minimum value
        self.level = 0  # Current level of the SkipList

    def search(self, target: int) -> bool:
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forward[i] and node.forward[i].value < target:
                node = node.forward[i]
        node = node.forward[0]
        return node and node.value == target

    def add(self, num: int) -> None:
        update = [None] * (self.max_level + 1)
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forward[i] and node.forward[i].value < num:
                node = node.forward[i]
            update[i] = node
        node = node.forward[0]
        
        if node and node.value == num:
            return  # Duplicate value, do nothing
        
        new_level = self.random_level()
        if new_level > self.level:
            for i in range(self.level + 1, new_level + 1):
                update[i] = self.head
            self.level = new_level
        
        new_node = SkipNode(num, new_level)
        for i in range(new_level + 1):
            new_node.forward[i] = update[i].forward[i]
            if update[i].forward[i]:
                update[i].forward[i].backward = new_node
            update[i].forward[i] = new_node
            new_node.backward = update[0]

    def erase(self, num: int) -> bool:
        update = [None] * (self.max_level + 1)
        node = self.head
        for i in range(self.level, -1, -1):
            while node.forward[i] and node.forward[i].value < num:
                node = node.forward[i]
            update[i] = node
        node = node.forward[0]
        
        if node and node.value == num:
            for i in range(self.level + 1):
                if update[i].forward[i] != node:
                    break
                update[i].forward[i] = node.forward[i]
                if node.forward[i]:
                    node.forward[i].backward = update[i]
            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1
            return True
        
        return False

    def random_level(self) -> int:
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level