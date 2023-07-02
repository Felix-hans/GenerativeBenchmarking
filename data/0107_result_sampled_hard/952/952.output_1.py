# @lc app=leetcode id=952 lang=python3
from typing import List
from math import isqrt

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        graph = [[] for _ in range(max_num + 1)]

        def get_prime_factors(num):
            factors = set()
            while num % 2 == 0:
                factors.add(2)
                num //= 2
            for i in range(3, isqrt(num) + 1, 2):
                while num % i == 0:
                    factors.add(i)
                    num //= i
            if num > 2:
                factors.add(num)
            return factors

        for num in nums:
            prime_factors = get_prime_factors(num)
            for factor in prime_factors:
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
                parent[rootX] = rootY
                size[rootY] += size[rootX]

        parent = [i for i in range(max_num + 1)]
        size = [1] * (max_num + 1)

        for num in nums:
            for factor in graph[num]:
                union(parent, size, num, factor)

        max_size = max(size)

        return max_size