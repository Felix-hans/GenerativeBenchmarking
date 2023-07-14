# @lc app=leetcode id=1656 lang=python3
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize the stream with empty values
        self.ptr = 0  # Pointer to keep track of the last inserted position

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Adjust idKey to 0-based index
        self.stream[idKey] = value  # Insert the value at the corresponding index

        result = []  # List to store the chunk of values
        if idKey == self.ptr:
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                result.append(self.stream[self.ptr])
                self.ptr += 1  # Move the pointer to the next position
        return result