# @lc app=leetcode id=952 lang=python3
class Solution:
    def largestComponentSize(self, nums):
        def find(parents, i):
            while parents[i] != i:
                parents[i] = parents[parents[i]]  # Path compression
                i = parents[i]
            return i

        def union(parents, sizes, i, j):
            root_i = find(parents, i)
            root_j = find(parents, j)
            if root_i != root_j:
                parents[root_j] = root_i
                sizes[root_i] += sizes[root_j]

        def get_factors(num):
            factors = set()
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.add(i)
                    factors.add(num // i)
            return factors

        n = len(nums)
        parents = list(range(n))
        sizes = [1] * n

        num_to_index = {num: i for i, num in enumerate(nums)}

        for num in nums:
            factors = get_factors(num)
            for factor in factors:
                if factor in num_to_index:
                    union(parents, sizes, num_to_index[num], num_to_index[factor])

        return max(sizes)