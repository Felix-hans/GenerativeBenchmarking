# @lc app=leetcode id=895 lang=python3
class FreqStack:
    def __init__(self):
        self.frequency = {}  # Dictionary to track the frequency of elements
        self.stack = []  # List to store the elements in the stack

    def push(self, val: int) -> None:
        if val in self.frequency:
            self.frequency[val] += 1
        else:
            self.frequency[val] = 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.frequency.values())  # Find the maximum frequency
        elements_with_max_freq = [x for x in self.stack if self.frequency[x] == max_freq]
        top_most_element = elements_with_max_freq[-1]  # Get the element closest to the stack's top
        self.frequency[top_most_element] -= 1  # Decrement the frequency of the popped element
        self.stack.remove(top_most_element)  # Remove the popped element from the stack
        return top_most_element