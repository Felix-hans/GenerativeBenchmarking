# @lc app=leetcode id=952 lang=python3
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.size[root_x] += self.size[root_y]

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        n = len(nums)
        uf = UnionFind(n)
        factors = {}

        for i, num in enumerate(nums):
            j = 2
            while j * j <= num:
                if num % j == 0:
                    if j not in factors:
                        factors[j] = i
                    else:
                        uf.union(i, factors[j])

                    if num // j not in factors:
                        factors[num // j] = i
                    else:
                        uf.union(i, factors[num // j])
                j += 1

            if num not in factors:
                factors[num] = i
            else:
                uf.union(i, factors[num])

        component_sizes = [0] * n
        for i in range(n):
            component_sizes[uf.find(i)] += 1

        return max(component_sizes)