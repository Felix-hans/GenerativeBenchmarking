# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.right = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.head = Node(float('-inf'))
        
    def search(self, target: int) -> bool:
        node = self.head
        while node:
            if node.val == target:
                return True
            elif node.val < target:
                node = node.right
            else:
                node = node.down
        return False
    
    def add(self, num: int) -> None:
        nodes = []
        node = self.head
        while node:
            while node.right and node.right.val < num:
                node = node.right
            nodes.append(node)
            node = node.down
        
        insert = True
        down = None
        while insert and nodes:
            node = nodes.pop()
            new_node = Node(num)
            new_node.right = node.right
            node.right = new_node
            new_node.down = down
            down = new_node
            insert = random.choice([True, False])
    
        if insert:
            new_node = Node(num)
            new_node.right = None
            new_node.down = down
            self.head = Node(float('-inf'))
            self.head.right = new_node
            
    def erase(self, num: int) -> bool:
        node = self.head
        found = False
        while node:
            while node.right and node.right.val < num:
                node = node.right
            if node.right and node.right.val == num:
                found = True
                node.right = node.right.right
            node = node.down
        return found