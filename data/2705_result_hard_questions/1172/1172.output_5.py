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

        value = self.stacks[self.rightmost].pop()

        if not self.stacks[self.rightmost]:
            self.rightmost -= 1

        return value

    def popAtStack(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1

        value = self.stacks[index].pop()

        if index < self.leftmost:
            self.leftmost = index

        return value


D = DinnerPlates(2)

D.push(1)
D.push(2)
D.push(3)
D.push(4)
D.push(5)

print(D.popAtStack(0))  # Output: 2
D.push(20)
D.push(21)
print(D.popAtStack(0))  # Output: 20
print(D.popAtStack(2))  # Output: 21
print(D.pop())         # Output: 5
print(D.pop())         # Output: 4
print(D.pop())         # Output: 3
print(D.pop())         # Output: 1
print(D.pop())         # Output: -1