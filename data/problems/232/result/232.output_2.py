# @lc app=leetcode id=232 lang=python3
class MyQueue:

    def __init__(self):
        self.stack1 = []  # For enqueue operation (push)
        self.stack2 = []  # For dequeue operation (pop)

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
        return len(self.stack1) == 0 and len(self.stack2) == 0