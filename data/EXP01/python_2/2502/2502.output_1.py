class Allocator:

    def __init__(self, n: int):
        self.memory = [None] * n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        start_index = -1
        for i, unit in enumerate(self.memory):
            if unit is None:
                count += 1
                if start_index == -1:
                    start_index = i
                if count == size:
                    for j in range(start_index, i+1):
                        self.memory[j] = mID
                    return start_index
            else:
                count = 0
                start_index = -1
        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i, unit in enumerate(self.memory):
            if unit == mID:
                self.memory[i] = None
                count += 1
        return count


