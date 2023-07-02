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
        max_freq_index = -1
        for candidate in candidates:
            for i in range(len(self.stack)-1, -1, -1):
                if self.stack[i] == candidate:
                    if i > max_freq_index:
                        max_freq_element = candidate
                        max_freq_index = i
                    break

        self.freq[max_freq_element] -= 1
        self.stack.pop(max_freq_index)

        return max_freq_element