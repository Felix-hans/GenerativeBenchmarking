# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(parent, x):
            if parent[x] != x:
                parent[x] = find(parent, parent[x])
            return parent[x]

        def union(parent, rank, x, y):
            x_root = find(parent, x)
            y_root = find(parent, y)

            if x_root != y_root:
                if rank[x_root] < rank[y_root]:
                    parent[x_root] = y_root
                    rank[y_root] += rank[x_root]
                else:
                    parent[y_root] = x_root
                    rank[x_root] += rank[y_root]

        max_num = max(nums)
        is_prime = [True] * (max_num + 1)
        primes = []

        for i in range(2, int(max_num ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, max_num + 1, i):
                    is_prime[j] = False

        for i in range(2, max_num + 1):
            if is_prime[i]:
                primes.append(i)

        parent = [i for i in range(max_num + 1)]
        rank = [1] * (max_num + 1)

        for num in nums:
            for prime in primes:
                if prime * prime > num:
                    break
                if num % prime == 0:
                    union(parent, rank, num, prime)
                    union(parent, rank, num, num // prime)

        component_sizes = {}
        largest_size = 0

        for num in nums:
            root = find(parent, num)
            component_sizes[root] = component_sizes.get(root, 0) + 1
            largest_size = max(largest_size, component_sizes[root])

        return largest_size