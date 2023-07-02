# @lc app=leetcode id=1172 lang=python3
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []  # List to store the stacks
        self.available_stacks = []  # List to store the available stack indices

    def push(self, val: int) -> None:
        if self.available_stacks:  # If there are available stacks
            stack_index = self.available_stacks[0]  # Get the leftmost available stack index
            stack = self.stacks[stack_index]  # Get the stack at the index
            stack.append(val)  # Push the value to the stack
            if len(stack) == self.capacity:  # If the stack is full after pushing the value
                self.available_stacks.pop(0)  # Remove the stack index from the available stack indices
        else:  # If there are no available stacks
            stack = [val]  # Create a new stack with the value
            self.stacks.append(stack)  # Add the stack to the list of stacks
            if len(stack) == self.capacity:  # If the stack is full after pushing the value
                self.available_stacks.append(len(self.stacks) - 1)  # Add the stack index to the available stack indices

    def pop(self) -> int:
        if not self.stacks:  # If there are no stacks
            return -1
        stack = self.stacks[-1]  # Get the rightmost stack
        val = stack.pop()  # Pop the value from the stack
        if not stack:  # If the stack becomes empty after popping the value
            self.stacks.pop()  # Remove the stack from the list of stacks
        if len(stack) == self.capacity - 1:  # If the stack becomes available after popping the value
            self.available_stacks.insert(0, len(self.stacks) - 1)  # Add the stack index to the available stack indices
        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:  # If the stack index is out of range or the stack is empty
            return -1
        stack = self.stacks[index]  # Get the stack at the index
        val = stack.pop()  # Pop the value from the stack
        if len(stack) == self.capacity - 1:  # If the stack becomes available after popping the value
            self.available_stacks.insert(0, index)  # Add the stack index to the available stack indices
        return val