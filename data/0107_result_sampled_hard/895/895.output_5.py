# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.stack = []
        self.frequency = defaultdict(int)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        self.frequency[val] += 1
        self.max_frequency = max(self.max_frequency, self.frequency[val])
        self.stack.append(val)

    def pop(self) -> int:
        pop_val = None
        for i in range(len(self.stack) - 1, -1, -1):
            if self.frequency[self.stack[i]] == self.max_frequency:
                pop_val = self.stack.pop(i)
                self.frequency[pop_val] -= 1
                break
        
        if pop_val is not None:
            if self.frequency[pop_val] == 0:
                self.max_frequency -= 1
        
        return pop_val if pop_val is not None else 0