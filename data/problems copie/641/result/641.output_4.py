# @lc app=leetcode id=641 lang=python3
class MyCircularDeque:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.front = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k
        self.queue[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.k
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k
        self.queue[self.rear] = None
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1) % self.k]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


myCircularDeque = MyCircularDeque(3)
print(myCircularDeque.insertLast(1))  # return True
print(myCircularDeque.insertLast(2))  # return True
print(myCircularDeque.insertFront(3))  # return True
print(myCircularDeque.insertFront(4))  # return False, the queue is full.
print(myCircularDeque.getRear())  # return 2
print(myCircularDeque.isFull())  # return True
print(myCircularDeque.deleteLast())  # return True
print(myCircularDeque.insertFront(4))  # return True
print(myCircularDeque.getFront())  # return 4