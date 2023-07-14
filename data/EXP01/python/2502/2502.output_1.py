# @lc app=leetcode id=2502 lang=python3
class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n  # initialize memory array with all units free

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    for j in range(i - size + 1, i + 1):
                        self.memory[j] = mID
                    return i - size + 1
            else:
                count = 0
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                count += 1
                self.memory[i] = 0
            else:
                if count > 0:
                    return count
                count = 0
        return count