# @lc app=leetcode id=2467 lang=python3
from typing import List

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adjacency_list = [[] for _ in range(len(amount))]
        for edge in edges:
            adjacency_list[edge[0]].append(edge[1])
            adjacency_list[edge[1]].append(edge[0])
        
        def dfs(node: int, parent: int) -> int:
            total_income = amount[node] // 2 # Alice's share of the gate at the current node
            
            for neighbor in adjacency_list[node]:
                if neighbor != parent: # Avoid going back to the parent node
                    neighbor_income = dfs(neighbor, node)
                    total_income += max(0, neighbor_income) # Only add positive incomes
            
            return total_income
        
        max_income = dfs(0, -1)
        
        return max_income