# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  # Stores the frequency of each element
        self.stack = []  # Stores the elements in the order they were pushed
        self.max_freq = 0  # Stores the maximum frequency
        self.max_freq_index = defaultdict(list)  # Stores the indices of elements with the maximum frequency

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.max_freq = max(self.max_freq, self.freq[val])
        self.stack.append(val)
        self.max_freq_index[self.freq[val]].append(len(self.stack) - 1)

    def pop(self) -> int:
        max_freq_elements = self.max_freq_index[self.max_freq]
        max_freq_element_index = max_freq_elements.pop()
        if not max_freq_elements:
            self.max_freq -= 1
        self.freq[self.stack[max_freq_element_index]] -= 1
        return self.stack.pop(max_freq_element_index)