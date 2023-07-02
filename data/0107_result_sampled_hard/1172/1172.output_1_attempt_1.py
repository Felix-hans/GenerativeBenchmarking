# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        if not self.available:
            self.stacks.append([])
            self.available.append(len(self.stacks) - 1)
        stack_idx = self.available[0]
        stack = self.stacks[stack_idx]
        stack.append(val)
        if len(stack) == self.capacity:
            self.available.pop(0)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        stack_idx = len(self.stacks) - 1
        return self.popAtStack(stack_idx)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        stack = self.stacks[index]
        val = stack.pop()
        if not stack:
            self.stacks.pop(index)
        if index < self.available[0]:
            self.available.insert(0, index)
        if index in self.available and not stack:
            self.available.remove(index)
        return val