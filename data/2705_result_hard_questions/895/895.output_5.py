# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.stack = []
        self.max_freq = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        freq = self.frequency[val]
        if freq > self.max_freq:
            self.max_freq = freq
        self.stack.append(val)

    def pop(self) -> int:
        element_to_pop = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.frequency[self.stack[i]] == self.max_freq:
                element_to_pop = i
                break
        
        val = self.stack.pop(element_to_pop)
        self.frequency[val] -= 1
        if self.frequency[val] == 0:
            del self.frequency[val]
        
        self.max_freq = max(self.frequency.values()) if self.frequency else 0
        
        return val