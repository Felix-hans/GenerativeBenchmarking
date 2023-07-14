# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq_count = defaultdict(int)
        self.stack = []

    def push(self, val: int) -> None:
        self.freq_count[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = 0
        max_freq_elements = []

        for element, freq in self.freq_count.items():
            if freq > max_freq:
                max_freq = freq
                max_freq_elements = [element]
            elif freq == max_freq:
                max_freq_elements.append(element)

        max_freq_index = -1
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freq_elements:
                max_freq_index = i
                break

        popped_element = self.stack.pop(max_freq_index)
        self.freq_count[popped_element] -= 1

        return popped_element