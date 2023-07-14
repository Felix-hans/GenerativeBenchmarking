# @lc app=leetcode id=2671 lang=python3
class FrequencyTracker:
    def __init__(self):
        self.frequency_dict = {}

    def add(self, number):
        if number in self.frequency_dict:
            self.frequency_dict[number] += 1
        else:
            self.frequency_dict[number] = 1

    def deleteOne(self, number):
        if number in self.frequency_dict:
            self.frequency_dict[number] -= 1
            if self.frequency_dict[number] == 0:
                del self.frequency_dict[number]

    def hasFrequency(self, frequency):
        return frequency in self.frequency_dict.values()