# @lc app=leetcode id=1206 lang=python3
import random

class SkiplistNode:
    def __init__(self, value):
        self.value = value
        self.next = []
        
class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(float('-inf'))
        
    def search(self, target: int) -> bool:
        curr = self.head
        for level in reversed(range(len(curr.next))):
            while curr.next[level] and curr.next[level].value < target:
                curr = curr.next[level]
                
        curr = curr.next[0]
        return curr is not None and curr.value == target
    
    def add(self, num: int) -> None:
        node = SkiplistNode(num)
        curr = self.head
        update = [None] * len(curr.next)
        
        for level in reversed(range(len(curr.next))):
            while curr.next[level] and curr.next[level].value < num:
                curr = curr.next[level]
            update[level] = curr
        
        for level in range(len(node.next), random_level()):
            update.append(self.head)
            self.head.next.append(None)
            
        for level in range(len(node.next)):
            node.next.append(update[level].next[level])
            update[level].next[level] = node
    
    def erase(self, num: int) -> bool:
        curr = self.head
        update = [None] * len(curr.next)
        
        for level in reversed(range(len(curr.next))):
            while curr.next[level] and curr.next[level].value < num:
                curr = curr.next[level]
            update[level] = curr
        
        curr = curr.next[0]
        
        if curr is not None and curr.value == num:
            for level in reversed(range(len(curr.next))):
                update[level].next[level] = curr.next[level]
            return True
        
        return False
    
def random_level():
    level = 1
    while random.random() < 0.5:
        level += 1
    return level