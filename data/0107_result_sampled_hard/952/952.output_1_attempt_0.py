# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        graph = [[] for _ in range(max_num + 1)]

        def get_factors(num):
            factors = set()
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            return factors

        for num in nums:
            factors = get_factors(num)
            for factor in factors:
                graph[num].append(factor)
                graph[factor].append(num)

        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, size, x, y):
            rootX = find(parent, x)
            rootY = find(parent, y)
            if rootX != rootY:
                if size[rootX] < size[rootY]:
                    parent[rootX] = rootY
                    size[rootY] += size[rootX]
                else:
                    parent[rootY] = rootX
                    size[rootX] += size[rootY]

        parent = [i for i in range(max_num + 1)]
        size = [1] * (max_num + 1)

        for num in nums:
            for factor in graph[num]:
                union(parent, size, num, factor)

        max_size = max(size)

        return max_size