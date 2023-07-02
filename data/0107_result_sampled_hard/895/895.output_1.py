# @lc app=leetcode id=895 lang=python3
class FreqStack:
    def __init__(self):
        self.freq = {}  # dictionary to track frequency of elements
        self.stack = []  # list to maintain the order of elements

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = 0
        max_freq_elements = []  # list to store elements with the maximum frequency
        for element, frequency in self.freq.items():
            if frequency > max_freq:
                max_freq = frequency
                max_freq_elements = [element]
            elif frequency == max_freq:
                max_freq_elements.append(element)

        max_freq_stack_indices = []
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freq_elements:
                max_freq_stack_indices.append(i)
                if self.stack[i] in self.freq:
                    self.freq[self.stack[i]] -= 1
                    if self.freq[self.stack[i]] == 0:
                        del self.freq[self.stack[i]]
                break

        popped_element = self.stack[max_freq_stack_indices[-1]]
        del self.stack[max_freq_stack_indices[-1]]

        return popped_element