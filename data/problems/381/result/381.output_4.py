# @lc app=leetcode id=381 lang=python3
import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.indexes = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.indexes[val].add(len(self.nums) - 1)
        return len(self.indexes[val]) == 1

    def remove(self, val: int) -> bool:
        if self.indexes[val]:
            idx = self.indexes[val].pop()
            last = self.nums[-1]
            self.nums[idx] = last
            self.indexes[last].add(idx)
            self.indexes[last].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)