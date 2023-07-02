# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.non_empty_stacks = set()
        
    def push(self, val: int) -> None:
        if not self.non_empty_stacks:
            self.stacks.append([])
        for stack in self.stacks:
            if len(stack) < self.capacity:
                stack.append(val)
                self.non_empty_stacks.add(stack)
                return
        
        new_stack = [val]
        self.stacks.append(new_stack)
        self.non_empty_stacks.add(new_stack)

    def pop(self) -> int:
        if not self.non_empty_stacks:
            return -1
        
        rightmost_stack = self.stacks[-1]
        val = rightmost_stack.pop()
        
        if not rightmost_stack:
            self.stacks.pop()
            self.non_empty_stacks.remove(rightmost_stack)
        
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks):
            return -1
        
        stack = self.stacks[index]
        if not stack:
            return -1
        
        val = stack.pop()
        
        if not stack:
            self.non_empty_stacks.remove(stack)
        
        return val