# @lc app=leetcode id=381 lang=python3
import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.positions = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.nums.append(val)
        self.positions[val].add(len(self.nums) - 1)
        return len(self.positions[val]) == 1

    def remove(self, val: int) -> bool:
        if self.positions[val]:
            last_element = self.nums[-1]
            val_positions = self.positions[val]
            last_position = len(self.nums) - 1

            last_element_positions = self.positions[last_element]
            replace_position = val_positions.pop()

            self.nums[replace_position] = last_element
            last_element_positions.remove(last_position)
            if replace_position != last_position:
                last_element_positions.add(replace_position)
            if not val_positions:
                del self.positions[val]
            self.nums.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.nums)