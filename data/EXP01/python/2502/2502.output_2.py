# @lc app=leetcode id=2502 lang=python3
class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n

    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.memory)-size+1):
            if all(self.memory[i+j] is None for j in range(size)):
                for j in range(size):
                    self.memory[i+j] = mID
                return i
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(len(self.memory)):
            if self.memory[i] == mID:
                self.memory[i] = None
                count += 1
        return count


loc = Allocator(10)
print(loc.allocate(1, 1))  # Output: 0
print(loc.allocate(1, 2))  # Output: 1
print(loc.allocate(1, 3))  # Output: 2
print(loc.free(2))  # Output: 1
print(loc.allocate(3, 4))  # Output: 3
print(loc.allocate(1, 1))  # Output: 1
print(loc.allocate(1, 1))  # Output: 6
print(loc.free(1))  # Output: 3
print(loc.allocate(10, 2))  # Output: -1
print(loc.free(7))  # Output: 0