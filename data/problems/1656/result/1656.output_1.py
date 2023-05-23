# @lc app=leetcode id=1656 lang=python3
from typing import List

class OrderedStream:
    def __init__(self, n: int):
        self.stream = [None] * n  # Initialize the stream with None values
        self.ptr = 0  # Pointer to keep track of the next available index

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey -= 1  # Convert idKey to 0-based index
        self.stream[idKey] = value  # Insert the value at the corresponding index

        if idKey == self.ptr:  # If the inserted idKey is the next expected one
            chunk = []
            while self.ptr < len(self.stream) and self.stream[self.ptr]:
                chunk.append(self.stream[self.ptr])
                self.ptr += 1  # Move the pointer to the next index

            return chunk

        return []  # If the inserted idKey is not the next expected one, return an empty list


os = OrderedStream(5)
print(os.insert(3, "ccccc"))  # Output: []
print(os.insert(1, "aaaaa"))  # Output: ["aaaaa"]
print(os.insert(2, "bbbbb"))  # Output: ["bbbbb", "ccccc"]
print(os.insert(5, "eeeee"))  # Output: []
print(os.insert(4, "ddddd"))  # Output: ["ddddd", "eeeee"]