# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.push_stack = []
        self.pop_stack = []

    def push(self, val: int) -> None:
        if self.push_stack:
            stack = self.push_stack.pop()
            stack.append(val)
            if len(stack) < self.capacity:
                self.pop_stack.append(stack)
        else:
            if self.pop_stack and len(self.pop_stack[-1]) < self.capacity:
                stack = self.pop_stack[-1]
                stack.append(val)
                if len(stack) == self.capacity:
                    self.pop_stack.pop()
            else:
                stack = [val]
                self.stacks.append(stack)
                if len(stack) < self.capacity:
                    self.pop_stack.append(stack)

    def pop(self) -> int:
        while self.pop_stack and not self.pop_stack[-1]:
            self.pop_stack.pop()
        if not self.pop_stack:
            return -1
        stack = self.pop_stack[-1]
        val = stack.pop()
        if len(stack) == self.capacity - 1:
            self.push_stack.append(stack)
        if not stack:
            self.pop_stack.pop()
        return val

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            stack = self.stacks[index]
            val = stack.pop()
            if len(stack) == self.capacity - 1:
                self.push_stack.append(stack)
            if not stack:
                self.stacks.pop(index)
            return val
        return -1