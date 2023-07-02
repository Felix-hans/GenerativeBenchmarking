# @lc app=leetcode id=1172 lang=python3
import heapq

class DinnerPlates:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.push_stack = []
        self.pop_stack = []

    def push(self, val: int) -> None:
        if self.pop_stack:
            index = heapq.heappop(self.pop_stack)
            self.stacks[index].append(val)
            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.push_stack, index)
        else:
            if self.push_stack:
                index = heapq.heappop(self.push_stack)
                self.stacks[index].append(val)
                if len(self.stacks[index]) == self.capacity:
                    heapq.heappush(self.pop_stack, index)
            else:
                self.stacks.append([val])
                if len(self.stacks[-1]) < self.capacity:
                    heapq.heappush(self.push_stack, len(self.stacks) - 1)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        index = len(self.stacks) - 1
        if index in self.push_stack and len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.push_stack, index)
        if not self.stacks[index]:
            self.stacks.pop()
        return val

    def popAtStack(self, index: int) -> int:
        if index < len(self.stacks) and self.stacks[index]:
            val = self.stacks[index].pop()
            if len(self.stacks[index]) < self.capacity:
                heapq.heappush(self.push_stack, index)
            return val
        return -1