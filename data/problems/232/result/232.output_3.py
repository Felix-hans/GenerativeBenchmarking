# @lc app=leetcode id=232 lang=python3
class MyQueue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def push(self, x: int) -> None:
        while self.dequeue_stack:
            self.enqueue_stack.append(self.dequeue_stack.pop())

        self.enqueue_stack.append(x)

    def pop(self) -> int:
        self._transfer_elements()

        return self.dequeue_stack.pop()

    def peek(self) -> int:
        self._transfer_elements()

        return self.dequeue_stack[-1]

    def empty(self) -> bool:
        return not self.enqueue_stack and not self.dequeue_stack

    def _transfer_elements(self) -> None:
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())