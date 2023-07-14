# @lc app=leetcode id=2467 lang=python3
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = {}
        for edge in edges:
            u, v = edge
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(curr, prev, income):
            if not graph[curr]:  # current node is a leaf node
                return income
            
            max_income = -float('inf')
            for neighbor in graph[curr]:
                if neighbor == prev:  # skip the previous node
                    continue
                if income >= 0:  # Alice pays her share for opening the gate
                    new_income = income + amount[curr] // 2
                else:  # Alice receives her share for opening the gate
                    new_income = income + amount[curr]
                max_income = max(max_income, dfs(neighbor, curr, new_income))
            
            return max_income
        
        return dfs(0, bob, 0)