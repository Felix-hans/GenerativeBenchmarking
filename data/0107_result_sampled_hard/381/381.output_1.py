# @lc app=leetcode id=381 lang=python3
import random

class RandomizedCollection:
    def __init__(self):
        self.collection = []  # List to store the elements
        self.indices = {}  # Dictionary to map elements to their indices

    def insert(self, val: int) -> bool:
        self.collection.append(val)  # Add the element to the end of the list
        if val in self.indices:
            self.indices[val].add(len(self.collection) - 1)
            return False
        else:
            self.indices[val] = {len(self.collection) - 1}
            return True

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index = self.indices[val].pop()
            if len(self.indices[val]) == 0:
                del self.indices[val]  # Remove the element from the dictionary

            if index != len(self.collection) - 1:
                last_element = self.collection[-1]
                self.collection[index] = last_element
                self.indices[last_element].remove(len(self.collection) - 1)
                self.indices[last_element].add(index)

            self.collection.pop()  # Remove the last element from the list
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.collection)