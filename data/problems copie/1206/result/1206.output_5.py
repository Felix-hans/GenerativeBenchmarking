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
    
    def search(self, target: int) -> bool:
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            elif curr.val < target:
                curr = curr.next
            else:
                curr = curr.down
        return False
    
    def add(self, num: int) -> None:
        nodes = []
        curr = self.head
        while curr:
            if curr.next is None or curr.next.val > num:
                nodes.append(curr)
                curr = curr.down
            else:
                curr = curr.next
        
        should_insert = True
        down_node = None
        while should_insert and nodes:
            node = nodes.pop()
            new_node = Node(num)
            new_node.next = node.next
            node.next = new_node
            if down_node:
                new_node.down = down_node
            down_node = new_node
            should_insert = random.random() < 0.5
    
        if should_insert:
            new_node = Node(num)
            new_node.down = self.head
            self.head = Node(float('-inf'))
            self.head.next = new_node
    
    def erase(self, num: int) -> bool:
        curr = self.head
        found = False
        while curr:
            if curr.next and curr.next.val == num:
                found = True
                curr.next = curr.next.next
                curr = curr.down
            elif curr.val < num:
                curr = curr.next
            else:
                curr = curr.down
        return found