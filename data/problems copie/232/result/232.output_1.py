# @lc app=leetcode id=232 lang=python3
class MyQueue:

    def __init__(self):
        self.stack1 = []  # Used to store elements in the order they are pushed
        self.stack2 = []  # Used to reverse the order of elements for queue-like behavior

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def peek(self) -> int:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2