# @lc app=leetcode id=381 lang=python3
import random

class RandomizedCollection:

    def __init__(self):
        self.nums = []  # List to store the elements
        self.indices = {}  # Dictionary to map elements to indices

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        if val in self.indices:
            self.indices[val].add(len(self.nums) - 1)
            return False
        else:
            self.indices[val] = {len(self.nums) - 1}
            return True

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val].pop()
            if len(self.indices[val]) == 0:
                del self.indices[val]
            last_val = self.nums[-1]
            self.nums[index] = last_val
            self.indices[last_val].remove(len(self.nums) - 1)
            if len(self.indices[last_val]) == 0:
                del self.indices[last_val]
            if index < len(self.nums) - 1:
                self.indices[last_val].add(index)
            self.nums.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.nums)