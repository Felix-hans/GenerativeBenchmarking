# @lc app=leetcode id=641 lang=python3
class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None

class MyCircularDeque:
    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = 0
        self.capacity = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = ListNode(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        new_node = ListNode(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            next_node = self.head.next
            next_node.prev = None
            self.head = next_node
        
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail = prev_node
        
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.head.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity