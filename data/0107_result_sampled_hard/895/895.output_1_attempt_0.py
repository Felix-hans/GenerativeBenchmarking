# @lc app=leetcode id=895 lang=python3
class FreqStack:

    def __init__(self):
        self.freq = {}  # Dictionary to store element frequencies
        self.stack = []  # List to store the stack

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1

        max_freq = max(self.freq.values())

        self.stack.append((val, self.freq[val], max_freq))

    def pop(self) -> int:
        max_freq = max(self.freq.values())
        max_freq_elements = [item for item in self.stack if item[1] == max_freq]

        max_freq_top = max_freq_elements[-1][0]

        self.freq[max_freq_top] -= 1

        self.stack.pop()

        return max_freq_top