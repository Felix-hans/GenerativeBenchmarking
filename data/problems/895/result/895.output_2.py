# @lc app=leetcode id=895 lang=python3
class FreqStack:

    def __init__(self):
        self.freq = {}  # Dictionary to store the frequency of elements
        self.stack = []  # List to represent the stack

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq.values())  # Find the maximum frequency
        max_freq_elements = []
        for key, value in self.freq.items():
            if value == max_freq:
                max_freq_elements.append(key)
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freq_elements:
                element = self.stack.pop(i)
                self.freq[element] -= 1
                if self.freq[element] == 0:
                    del self.freq[element]
                return element

freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())  # Output: 5
print(freqStack.pop())  # Output: 7
print(freqStack.pop())  # Output: 5
print(freqStack.pop())  # Output: 4