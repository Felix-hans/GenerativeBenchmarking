# @lc app=leetcode id=952 lang=python3
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            return parents[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parents[root_x] = root_y
                sizes[root_y] += sizes[root_x]

        max_num = max(nums)
        parents = list(range(max_num + 1))
        sizes = [1] * (max_num + 1)

        for num in nums:
            for factor in range(2, int(num ** 0.5) + 1):
                if num % factor == 0:
                    union(num, factor)
                    union(num, num // factor)

        max_size = max(sizes)

        return max_size