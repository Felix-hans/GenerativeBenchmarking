# @lc app=leetcode id=381 lang=python3
import random

class RandomizedCollection:

    def __init__(self):
        self.collection = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        self.collection.append(val)
        if val in self.index_map:
            self.index_map[val].add(len(self.collection) - 1)
            return False
        else:
            self.index_map[val] = {len(self.collection) - 1}
            return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        index = self.index_map[val].pop()
        if not self.index_map[val]:
            del self.index_map[val]

        last_val = self.collection[-1]
        self.collection[index] = last_val
        self.index_map[last_val].remove(len(self.collection) - 1)
        self.index_map[last_val].add(index)

        self.collection.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.collection)