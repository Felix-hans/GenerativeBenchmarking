# @lc app=leetcode id=895 lang=python3
class FreqStack:
    def __init__(self):
        self.freq_dict = {}
        self.stack_list = [[]]

    def push(self, val: int) -> None:
        if val in self.freq_dict:
            freq = self.freq_dict[val] + 1
            self.freq_dict[val] = freq
        else:
            freq = 1
            self.freq_dict[val] = freq

        if freq == len(self.stack_list):
            self.stack_list.append([val])
        else:
            self.stack_list[freq].append(val)

    def pop(self) -> int:
        most_freq_stack = self.stack_list[-1]
        val = most_freq_stack.pop()
        
        freq = self.freq_dict[val] - 1
        if freq == 0:
            del self.freq_dict[val]
        else:
            self.freq_dict[val] = freq

        if len(most_freq_stack) == 0 and len(self.stack_list) > 1:
            self.stack_list.pop()

        return val