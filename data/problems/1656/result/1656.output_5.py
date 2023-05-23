# @lc app=leetcode id=1656 lang=python3
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize a list of size n to store the stream values
        self.ptr = 0  # Pointer to keep track of the next empty slot in the stream

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Adjust idKey to 0-based index
        self.stream[idKey] = value  # Insert the value at the corresponding index

        if idKey == self.ptr:
            chunk = []
            while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1
            return chunk

        return []  # Return an empty list if the inserted value does not complete a chunk


os = OrderedStream(5)
print(os.insert(3, "ccccc"))  # []
print(os.insert(1, "aaaaa"))  # ['aaaaa']
print(os.insert(2, "bbbbb"))  # ['bbbbb', 'ccccc']
print(os.insert(5, "eeeee"))  # []
print(os.insert(4, "ddddd"))  # ['ddddd', 'eeeee']