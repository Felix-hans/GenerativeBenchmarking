# @lc app=leetcode id=895 lang=python3
from collections import defaultdict

class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)  # Stores the frequency of each element
        self.stack = []  # Stores the elements in the order they were pushed

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq.values())  # Find the maximum frequency
        candidates = [x for x in self.stack if self.freq[x] == max_freq]  # Find elements with maximum frequency

        max_freq_element = None
        max_freq_index = len(self.stack)
        for candidate in candidates:
            index = len(self.stack) - 1 - self.stack[::-1].index(candidate)
            if index < max_freq_index:
                max_freq_element = candidate
                max_freq_index = index

        self.freq[max_freq_element] -= 1
        self.stack.remove(max_freq_element)

        return max_freq_element