# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # List of stacks
        self.non_empty_stacks = []  # List of non-empty stack indices

    def push(self, val: int) -> None:
        if not self.non_empty_stacks:
            self.stacks.append([val])
            self.non_empty_stacks.append(len(self.stacks) - 1)
        else:
            stack_index = self.non_empty_stacks[0]
            if len(self.stacks[stack_index]) == self.capacity:
                self.stacks.append([val])
                self.non_empty_stacks.append(len(self.stacks) - 1)
            else:
                self.stacks[stack_index].append(val)
                if len(self.stacks[stack_index]) == self.capacity:
                    self.non_empty_stacks.pop(0)

    def pop(self) -> int:
        if not self.non_empty_stacks:
            return -1

        stack_index = self.non_empty_stacks[-1]
        value = self.stacks[stack_index].pop()
        if not self.stacks[stack_index]:
            self.non_empty_stacks.pop()
        return value

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        value = self.stacks[index].pop()
        if len(self.stacks[index]) == self.capacity - 1:
            self.non_empty_stacks.append(index)

        return value