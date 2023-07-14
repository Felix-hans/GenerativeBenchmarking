# @lc app=leetcode id=2497 lang=python3
from typing import List

class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        adj_list = {}
        for u, v in edges:
            if u not in adj_list:
                adj_list[u] = []
            if v not in adj_list:
                adj_list[v] = []
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        nodes = sorted(range(len(vals)), key=lambda x: vals[x], reverse=True)
        
        max_sum = float('-inf')
        
        for center in nodes:
            total_sum = vals[center]
            edge_count = 0
            
            for neighbor in adj_list[center]:
                total_sum += vals[neighbor]
                edge_count += 1
                
                if edge_count > k:
                    break
            
            max_sum = max(max_sum, total_sum)
        
        return max_sum