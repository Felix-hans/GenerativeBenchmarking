# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('inf'))
        self.head.right = self.tail
        self.levels = 1
    
    def search(self, target: int) -> bool:
        node = self.head
        while node:
            while node.right.val < target:
                node = node.right
            if node.right.val == target:
                return True
            node = node.down
        return False
    
    def add(self, num: int) -> None:
        nodes = []
        node = self.head
        while node:
            while node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down
        
        insert_above = True
        down = None
        while insert_above and nodes:
            node = nodes.pop()
            new_node = Node(num)
            new_node.down = down
            down = new_node
            new_node.right = node.right
            node.right = new_node
            insert_above = random.random() < 0.5
            if insert_above:
                new_up_node = Node(num)
                new_up_node.down = down
                down = new_up_node
                new_up_node.right = node.right
                node.right = new_up_node
                node = new_up_node
                if len(nodes) == 0:
                    self.head = Node(float('-inf'))
                    self.head.right = new_up_node
                    self.head.down = self.tail
                    self.tail = Node(float('inf'))
                    self.tail.down = self.head
                    self.tail.right = new_up_node
                    self.levels += 1
    
    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            while node.right.val < num:
                node = node.right
            if node.right.val == num:
                found = True
                node.right = node.right.right
            node = node.down
        return found