# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # Dictionary to store the frequency of elements
        self.stack = []  # Stack to store the elements
        
    def push(self, val: int) -> None:
        self.freq[val] += 1  # Increment the frequency of the element
        self.stack.append(val)  # Add the element to the stack
        
    def pop(self) -> int:
        max_freq = max(self.freq.values())  # Find the maximum frequency
        
        for i in range(len(self.stack) - 1, -1, -1):
            if self.freq[self.stack[i]] == max_freq:
                self.freq[self.stack[i]] -= 1  # Decrement the frequency of the element
                return self.stack.pop(i)  # Remove and return the element
        
        return None  # Return None if the stack is empty