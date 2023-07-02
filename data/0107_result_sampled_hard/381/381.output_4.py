# @lc app=leetcode id=381 lang=python3
import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.nums = []  # List to store the numbers
        self.indices = defaultdict(set)  # Dictionary to store indices of numbers

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.indices[val].add(len(self.nums) - 1)
        return len(self.indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.indices or len(self.indices[val]) == 0:
            return False

        val_indices = self.indices[val]
        index_to_remove = val_indices.pop()

        last_num = self.nums[-1]
        last_num_indices = self.indices[last_num]
        last_num_indices.add(index_to_remove)
        last_num_indices.discard(len(self.nums) - 1)

        self.nums[index_to_remove] = last_num
        self.nums.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)