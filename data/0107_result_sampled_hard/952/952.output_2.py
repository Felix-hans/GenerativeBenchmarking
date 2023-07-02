# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parents[rootY] = rootX
                sizes[rootX] += sizes[rootY]

        max_num = max(nums)
        parents = [i for i in range(max_num + 1)]
        sizes = [1] * (max_num + 1)

        for num in nums:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    union(num, factor)
                    union(num, num // factor)

        component_sizes = [0] * (max_num + 1)
        largest_size = 0

        for num in nums:
            root = find(num)
            component_sizes[root] += 1
            largest_size = max(largest_size, component_sizes[root])

        return largest_size