# @lc app=leetcode id=2502 lang=python3
class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n

    def allocate(self, size: int, mID: int) -> int:
        start = -1
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                if count == 0:
                    start = i
                count += 1
                if count == size:
                    for j in range(start, start + size):
                        self.memory[j] = mID
                    return start
            else:
                count = 0
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = None
                count += 1
        return count