# @lc app=leetcode id=2671 lang=python3
class FrequencyTracker:

    def __init__(self):
        self.data = {}

    def add(self, number: int) -> None:
        if number in self.data:
            self.data[number] += 1
        else:
            self.data[number] = 1

    def deleteOne(self, number: int) -> None:
        if number in self.data:
            self.data[number] -= 1
            if self.data[number] == 0:
                del self.data[number]

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.data.values()