# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # List to store the stacks
        self.available = []  # List to store the indices of available stacks

    def push(self, val: int) -> None:
        if not self.available:
            self.stacks.append([])
            self.available.append(len(self.stacks) - 1)
        stack_index = self.available[0]
        stack = self.stacks[stack_index]
        stack.append(val)
        if len(stack) == self.capacity:
            self.available.pop(0)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        stack_index = len(self.stacks) - 1
        stack = self.stacks[stack_index]
        val = stack.pop()
        if not stack:
            self.stacks.pop(stack_index)
            if stack_index in self.available:
                self.available.remove(stack_index)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        stack = self.stacks[index]
        if not stack:
            return -1
        val = stack.pop()
        if index not in self.available:
            self.available.insert(0, index)
        return val