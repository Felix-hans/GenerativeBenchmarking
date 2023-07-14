# @lc app=leetcode id=1206 lang=python3
import random

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.down = None

class Skiplist:
    def __init__(self):
        self.levels = [Node()]  # Start with one level containing a sentinel node
    
    def search(self, target: int) -> bool:
        curr = self.levels[-1]  # Start from the top level
        while curr:
            if curr.next and curr.next.val < target:
                curr = curr.next
            elif curr.next and curr.next.val == target:
                return True
            else:
                curr = curr.down
        return False
    
    def add(self, num: int) -> None:
        level = 1
        while random.random() < 0.5:
            level += 1
        while len(self.levels) < level:
            new_level = Node()
            new_level.down = self.levels[-1]
            self.levels.append(new_level)
        curr = self.levels[-1]  # Start from the top level
        prev = None
        while curr:
            if curr.next and curr.next.val < num:
                curr = curr.next
            else:
                new_node = Node(num)
                new_node.next = curr.next
                curr.next = new_node
                if prev:
                    prev.down = new_node
                prev = new_node
                curr = curr.down
    
    def erase(self, num: int) -> bool:
        found = False
        curr = self.levels[-1]  # Start from the top level
        while curr:
            if curr.next and curr.next.val < num:
                curr = curr.next
            elif curr.next and curr.next.val == num:
                found = True
                curr.next = curr.next.next
                curr = curr.down
            else:
                curr = curr.down
        return found