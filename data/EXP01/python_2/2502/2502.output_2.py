class Allocator:

    def __init__(self, n: int):
        self.memory = [0] * n
        self.block_dict = {}
    
    def allocate(self, size: int, mID: int) -> int:
        for i in range(len(self.memory)):
            if self.memory[i] == 0:
                available = True
                for j in range(size):
                    if i+j >= len(self.memory) or self.memory[i+j] != 0:
                        available = False
                        break
                if available:
                    for j in range(size):
                        self.memory[i+j] = mID
                    if mID in self.block_dict:
                        self.block_dict[mID].append(i)
                    else:
                        self.block_dict[mID] = [i]
                    return i
        return -1
    
    def free(self, mID: int) -> int:
        if mID in self.block_dict:
            count = 0
            for block in self.block_dict[mID]:
                for i in range(block, len(self.memory)):
                    if self.memory[i] == mID:
                        self.memory[i] = 0
                        count += 1
                    else:
                        break
            del self.block_dict[mID]
            return count
        return 0
