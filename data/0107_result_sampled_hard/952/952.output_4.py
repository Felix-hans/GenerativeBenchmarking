# @lc app=leetcode id=952 lang=python3
from typing import List

class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        max_num = max(nums)
        
        parent = list(range(max_num + 1))
        
        for num in nums:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    self.union(parent, num, i)
                    self.union(parent, num, num // i)
        
        component_sizes = {}
        for num in nums:
            component = self.find(parent, num)
            component_sizes[component] = component_sizes.get(component, 0) + 1
        
        return max(component_sizes.values())
    
    def union(self, parent: List[int], x: int, y: int) -> None:
        parent_x = self.find(parent, x)
        parent_y = self.find(parent, y)
        if parent_x != parent_y:
            parent[parent_x] = parent_y
    
    def find(self, parent: List[int], x: int) -> int:
        if parent[x] != x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]