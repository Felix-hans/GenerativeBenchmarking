# @lc app=leetcode id=2497 lang=python3
from typing import List

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        n = len(vals)
        adj_list = [[] for _ in range(n)]  # adjacency list representation of the graph
        for edge in edges:
            u, v = edge
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        max_sum = float('-inf')
        
        def dfs(node, parent):
            nonlocal max_sum
            
            sum_with_node = vals[node]
            num_edges = 0
            
            for neighbor in adj_list[node]:
                if neighbor == parent:
                    continue
                sum_with_neighbor, num_edges_with_neighbor = dfs(neighbor, node)
                sum_with_node += sum_with_neighbor
                num_edges += num_edges_with_neighbor + 1
            
            if num_edges <= k:
                max_sum = max(max_sum, sum_with_node)
            
            return sum_with_node, num_edges
        
        dfs(0, -1)  # Start the DFS from node 0
        
        return max_sum