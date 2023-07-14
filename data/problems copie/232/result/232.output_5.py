# @lc app=leetcode id=232 lang=python3
class MyQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        self.stack_push.append(x)

    def transfer_elements(self):
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())

    def pop(self) -> int:
        if not self.stack_pop:
            self.transfer_elements()
        return self.stack_pop.pop()

    def peek(self) -> int:
        if not self.stack_pop:
            self.transfer_elements()
        return self.stack_pop[-1]

    def empty(self) -> bool:
        return not self.stack_push and not self.stack_pop