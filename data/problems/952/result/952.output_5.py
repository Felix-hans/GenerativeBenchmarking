# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        uf = UnionFind(max_num + 1)  # +1 to account for 0-based indexing
        
        for num in nums:
            for factor in range(2, int(num**0.5) + 1):
                if num % factor == 0:
                    uf.union(num, factor)
                    uf.union(num, num // factor)
        
        component_sizes = [0] * (max_num + 1)
        max_size = 0
        for num in nums:
            component_id = uf.find(num)
            component_sizes[component_id] += 1
            max_size = max(max_size, component_sizes[component_id])
        
        return max_size


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1