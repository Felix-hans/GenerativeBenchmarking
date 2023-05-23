# @lc app=leetcode id=952 lang=python3
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.size[rootX] < self.size[rootY]:
                rootX, rootY = rootY, rootX
            self.parent[rootY] = rootX
            self.size[rootX] += self.size[rootY]

class Solution:
    def largestComponentSize(self, nums):
        def primeFactors(num):
            factors = set()
            while num % 2 == 0:
                factors.add(2)
                num //= 2
            i = 3
            while i * i <= num:
                if num % i == 0:
                    factors.add(i)
                    num //= i
                else:
                    i += 2
            if num > 1:
                factors.add(num)
            return factors

        n = len(nums)
        uf = UnionFind(n)
        primeToIndex = {}
        for i, num in enumerate(nums):
            factors = primeFactors(num)
            for factor in factors:
                if factor in primeToIndex:
                    uf.union(i, primeToIndex[factor])
                primeToIndex[factor] = i

        return max(uf.size)