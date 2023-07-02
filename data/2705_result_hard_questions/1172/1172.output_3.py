# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.non_empty_stacks = set()
        self.empty_indices = []
        
    def push(self, val: int) -> None:
        if not self.non_empty_stacks:
            if self.empty_indices:
                stack_index = self.empty_indices.pop(0)
                self.stacks[stack_index] = []
                self.stacks[stack_index].append(val)
                self.non_empty_stacks.add(stack_index)
            else:
                self.stacks.append([val])
                self.non_empty_stacks.add(len(self.stacks) - 1)
        else:
            stack_index = min(self.non_empty_stacks)
            stack = self.stacks[stack_index]
            stack.append(val)
            if len(stack) == self.capacity:
                self.non_empty_stacks.remove(stack_index)

    def pop(self) -> int:
        if not self.non_empty_stacks:
            return -1
        
        stack_index = max(self.non_empty_stacks)
        stack = self.stacks[stack_index]
        val = stack.pop()
        if not stack:
            self.non_empty_stacks.remove(stack_index)
            self.empty_indices.append(stack_index)
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or index not in self.non_empty_stacks:
            return -1
        
        stack = self.stacks[index]
        val = stack.pop()
        if not stack:
            self.non_empty_stacks.remove(index)
            self.empty_indices.append(index)
        return val