# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def get_factors(num):
            factors = set()
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            return factors

        class UnionFind:
            def __init__(self, n):
                self.parent = list(range(n))
                self.size = [1] * n

            def find(self, x):
                if self.parent[x] != x:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                root_x = self.find(x)
                root_y = self.find(y)
                if root_x != root_y:
                    if self.size[root_x] < self.size[root_y]:
                        self.parent[root_x] = root_y
                        self.size[root_y] += self.size[root_x]
                    else:
                        self.parent[root_y] = root_x
                        self.size[root_x] += self.size[root_y]

        uf = UnionFind(len(nums))
        num_index = {}
        for i, num in enumerate(nums):
            num_index[num] = i

        for num in nums:
            factors = get_factors(num)
            for factor in factors:
                if factor in num_index:
                    uf.union(num_index[num], num_index[factor])

        return max(uf.size)