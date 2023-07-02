# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.available = []

    def push(self, val: int) -> None:
        if self.available:
            index = self.available[0]
            self.stacks[index].append(val)
            if len(self.stacks[index]) == self.capacity:
                self.available.pop(0)
        else:
            if not self.stacks or len(self.stacks[-1]) == self.capacity:
                self.stacks.append([])
            self.stacks[-1].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        return self.stacks[-1].pop()

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1
        return self.stacks[index].pop()

        if len(self.stacks[index]) == self.capacity - 1:
            self.available.insert(0, index)