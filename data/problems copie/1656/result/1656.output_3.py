# @lc app=leetcode id=1656 lang=python3
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize a list to store the stream
        self.ptr = 0  # Pointer to keep track of the next available index

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Adjust idKey to be zero-based
        self.stream[idKey] = value  # Insert the (idKey, value) pair into the stream
        result = []

        while self.ptr < len(self.stream) and self.stream[self.ptr] is not None:
            result.append(self.stream[self.ptr])  # Add the value to the result
            self.ptr += 1  # Move the pointer forward

        return result