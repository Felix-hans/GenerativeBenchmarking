# @lc app=leetcode id=2671 lang=python3
class FrequencyTracker:
    def __init__(self):
        self.num_dict = {}
        self.num_list = []

    def add(self, number: int) -> None:
        self.num_dict[number] = self.num_dict.get(number, 0) + 1
        self.num_list.append(number)

    def deleteOne(self, number: int) -> None:
        if number in self.num_dict:
            self.num_dict[number] -= 1
            if self.num_dict[number] == 0:
                del self.num_dict[number]
            self.num_list.remove(number)

    def hasFrequency(self, frequency: int) -> bool:
        for num in self.num_dict:
            if self.num_dict[num] == frequency:
                return True
        return False