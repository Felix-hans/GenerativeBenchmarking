# @lc app=leetcode id=2502 lang=python
class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n
        self.allocations = {}

    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.memory)):
            if self.memory[i] is None:
                if i + size <= len(self.memory):
                    if all(x is None for x in self.memory[i:i+size]):
                        for j in range(i, i+size):
                            self.memory[j] = mID
                        if mID not in self.allocations:
                            self.allocations[mID] = []
                        self.allocations[mID].append((i, size))
                        return i
        return -1

    def free(self, mID: int) -> int:
        if mID in self.allocations:
            freed_memory = 0
            for allocation in self.allocations[mID]:
                start, size = allocation
                for i in range(start, start+size):
                    if self.memory[i] == mID:
                        self.memory[i] = None
                        freed_memory += 1
            del self.allocations[mID]
            return freed_memory
        else:
            return 0