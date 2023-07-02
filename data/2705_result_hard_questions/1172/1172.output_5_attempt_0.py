# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # List of stacks
        self.leftmost = 0  # Leftmost non-empty stack index
        self.rightmost = -1  # Rightmost non-empty stack index

    def push(self, val: int) -> None:
        if not self.stacks or len(self.stacks[self.rightmost]) == self.capacity:
            self.stacks.append([])  
            self.rightmost += 1

        self.stacks[self.rightmost].append(val)

    def pop(self) -> int:
        if not self.stacks:
            return -1

        while self.rightmost >= 0 and not self.stacks[self.rightmost]:
            self.rightmost -= 1

        if self.rightmost < 0:
            return -1

        return self.stacks[self.rightmost].pop()

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        return self.stacks[index].pop()