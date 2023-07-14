# @lc app=leetcode id=952 lang=python3
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        dsu = DSU(max(nums))

        for num in nums:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    dsu.union(num, factor)
                    dsu.union(num, num // factor)

        component_count = {}
        max_size = 0

        for num in nums:
            root = dsu.find(num)
            component_count[root] = component_count.get(root, 0) + 1
            max_size = max(max_size, component_count[root])

        return max_size


class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
            self.rank[root_y] += self.rank[root_x]
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += self.rank[root_y]