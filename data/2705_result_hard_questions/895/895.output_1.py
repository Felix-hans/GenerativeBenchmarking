# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.freq_stack = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        freq = self.freq[val]
        self.max_freq = max(self.max_freq, freq)
        self.freq_stack[freq].append(val)

    def pop(self) -> int:
        val = self.freq_stack[self.max_freq].pop()
        self.freq[val] -= 1
        if not self.freq_stack[self.max_freq]:
            self.max_freq -= 1
        return val