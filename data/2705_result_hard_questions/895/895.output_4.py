# @lc app=leetcode id=895 lang=python3
class FreqStack:
    def __init__(self):
        self.freq = {}  # Dictionary to store the frequency of each element
        self.stack = []  # List to store the elements in the stack

    def push(self, val: int) -> None:
        if val in self.freq:
            self.freq[val] += 1
        else:
            self.freq[val] = 1
        self.stack.append(val)

    def pop(self) -> int:
        max_freq = max(self.freq.values())  # Find the maximum frequency
        max_freq_elements = [key for key, value in self.freq.items() if value == max_freq]  # Find elements with maximum frequency
        element_to_pop = None

        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] in max_freq_elements:
                element_to_pop = self.stack[i]
                del self.stack[i]
                break

        self.freq[element_to_pop] -= 1

        if self.freq[element_to_pop] == 0:
            del self.freq[element_to_pop]

        return element_to_pop