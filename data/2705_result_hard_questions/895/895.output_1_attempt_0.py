# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq.values())
        candidates = [x for x in self.stack if self.freq[x] == max_freq]
        element_to_pop = candidates.pop()
        self.freq[element_to_pop] -= 1
        if self.freq[element_to_pop] == 0:
            del self.freq[element_to_pop]
        self.stack.remove(element_to_pop)
        return element_to_pop