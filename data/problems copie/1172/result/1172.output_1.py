# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = [[]]  # Initialize with one empty stack

    def push(self, val: int) -> None:
        for stack in self.stacks:
            if len(stack) < self.capacity:
                stack.append(val)
                return
        self.stacks.append([val])

    def pop(self) -> int:
        for stack in reversed(self.stacks):
            if stack:
                val = stack.pop()
                if not stack:
                    self.stacks.pop()
                return val
        return -1  # All stacks are empty

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            val = self.stacks[index].pop()
            return val
        return -1  # The stack at the given index is empty