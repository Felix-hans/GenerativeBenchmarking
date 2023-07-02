# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None, right=None, down=None):
        self.val = val
        self.right = right
        self.down = down

class Skiplist:
    def __init__(self):
        self.head = Node()
        
    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            while curr.right and curr.right.val < target:
                curr = curr.right
            if curr.right and curr.right.val == target:
                return True
            curr = curr.down
        return False
        
    def add(self, num: int) -> None:
        nodes = []
        curr = self.head
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            nodes.append(curr)
            curr = curr.down
        
        insert = True
        down = None
        while insert and nodes:
            curr = nodes.pop()
            curr.right = Node(num, curr.right, down)
            down = curr.right
            insert = random.random() < 0.5
        
        if insert:
            self.head = Node(None, Node(num, None, down), self.head)
        
    def erase(self, num: int) -> bool:
        curr = self.head
        erased = False
        while curr:
            while curr.right and curr.right.val < num:
                curr = curr.right
            if curr.right and curr.right.val == num:
                curr.right = curr.right.right
                erased = True
            curr = curr.down
        return erased