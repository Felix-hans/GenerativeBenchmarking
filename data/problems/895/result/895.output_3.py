# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # Frequency dictionary
        self.stack = []  # Stack to store elements

    def push(self, val: int) -> None:
        self.freq[val] += 1  # Increment the frequency of the element
        self.stack.append(val)  # Add the element to the stack

    def pop(self) -> int:
        max_freq = max(self.freq.values())  # Find the maximum frequency
        elements_with_max_freq = [x for x in self.stack if self.freq[x] == max_freq]  # Find elements with maximum frequency
        top_element = None

        for element in reversed(self.stack):  # Iterate over the stack in reverse order
            if element in elements_with_max_freq:  # Check if the element has maximum frequency
                top_element = element
                self.freq[element] -= 1  # Decrement the frequency of the element
                if self.freq[element] == 0:  # If the frequency becomes 0, remove it from the frequency dictionary
                    del self.freq[element]
                self.stack.remove(element)  # Remove the element from the stack
                break

        return top_element