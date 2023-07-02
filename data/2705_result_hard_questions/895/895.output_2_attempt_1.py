# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.stack = []
        self.freq = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        if self.freq[val] > self.max_freq:
            self.max_freq = self.freq[val]
        self.stack.append(val)

    def pop(self) -> int:
        max_freq_elements = [x for x in self.stack if self.freq[x] == self.max_freq]
        if not max_freq_elements:
            return None
        element = max_freq_elements.pop()
        self.freq[element] -= 1
        if not max_freq_elements:
            self.max_freq -= 1
        self.stack.pop(self.stack.index(element))
        return element