# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.stacks = []
        self.capacity = capacity
        self.available = []

    def push(self, val: int) -> None:
        if self.available:
            stack_index = self.available[0]
            self.stacks[stack_index].append(val)
            if len(self.stacks[stack_index]) == self.capacity:
                self.available.pop(0)
        else:
            if not self.stacks or len(self.stacks[-1]) == self.capacity:
                self.stacks.append([])
            self.stacks[-1].append(val)
            if len(self.stacks[-1]) < self.capacity:
                self.available.append(len(self.stacks) - 1)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if index < len(self.stacks) - 1 and index not in self.available:
            self.available.insert(0, index)
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return val