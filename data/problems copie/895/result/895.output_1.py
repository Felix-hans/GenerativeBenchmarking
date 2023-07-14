# @lc app=leetcode id=895 lang=python3
from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.stack = []
        self.freq_counter = defaultdict(int)
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.freq_counter[val] += 1
        freq = self.freq_counter[val]
        if freq > self.max_freq:
            self.max_freq = freq
        self.stack.append((val, freq))

    def pop(self) -> int:
        max_freq_items = [item for item in self.stack if item[1] == self.max_freq]
        val_to_pop = max_freq_items.pop()
        self.freq_counter[val_to_pop[0]] -= 1
        if not max_freq_items:
            self.max_freq -= 1
        self.stack.remove(val_to_pop)
        return val_to_pop[0]