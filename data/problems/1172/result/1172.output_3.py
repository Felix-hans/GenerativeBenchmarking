# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available_stacks = []

    def push(self, val: int) -> None:
        if not self.available_stacks:
            self.stacks.append([])
            self.available_stacks.append(len(self.stacks) - 1)
        stack_index = self.available_stacks[0]
        stack = self.stacks[stack_index]
        stack.append(val)
        if len(stack) == self.capacity:
            self.available_stacks.pop(0)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        stack_index = len(self.stacks) - 1
        return self.popAtStack(stack_index)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        stack = self.stacks[index]
        val = stack.pop()
        if index not in self.available_stacks:
            self.available_stacks.append(index)
        return val