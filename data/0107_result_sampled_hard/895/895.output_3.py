# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)  # Frequency dictionary
        self.stack = []  # Stack to store elements
        self.max_freq = 0  # Maximum frequency encountered so far

    def push(self, val: int) -> None:
        self.freq[val] += 1  # Increment frequency of the element
        freq = self.freq[val]  # Get the updated frequency

        self.max_freq = max(self.max_freq, freq)

        if freq > len(self.stack):
            self.stack.append([val])
        else:
            self.stack[freq - 1].append(val)

    def pop(self) -> int:
        val = self.stack[self.max_freq - 1].pop()

        self.freq[val] -= 1

        if not self.stack[self.max_freq - 1]:
            self.max_freq -= 1

        return val