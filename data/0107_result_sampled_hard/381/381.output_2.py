# @lc app=leetcode id=381 lang=python3
import random

class RandomizedCollection:

    def __init__(self):
        self.collection = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        self.collection.append(val)
        if val in self.indices:
            self.indices[val].append(len(self.collection) - 1)
            return False
        else:
            self.indices[val] = [len(self.collection) - 1]
            return True

    def remove(self, val: int) -> bool:
        if val in self.indices:
            last_element = self.collection[-1]
            index_to_remove = self.indices[val].pop()
            if not self.indices[val]:
                del self.indices[val]
            if index_to_remove != len(self.collection) - 1:
                self.collection[index_to_remove] = last_element
                self.indices[last_element].remove(len(self.collection) - 1)
                self.indices[last_element].append(index_to_remove)
            self.collection.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.collection)