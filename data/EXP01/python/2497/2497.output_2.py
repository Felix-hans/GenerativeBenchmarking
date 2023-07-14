# @lc app=leetcode id=2497 lang=python3
class Solution:
    def maxStarSum(self, vals, edges, k):
        graph = [[] for _ in range(len(vals))]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        self.max_sum = float('-inf')  # Initialize maximum star sum
        
        def dfs(node, visited, edge_count, s):
            visited[node] = True
            s += vals[node]
            
            if edge_count > k:
                return
            
            if edge_count <= k:
                self.max_sum = max(self.max_sum, s)
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, edge_count + 1, s)
            
            visited[node] = False
        
        for i in range(len(vals)):
            visited = [False] * len(vals)
            dfs(i, visited, 0, 0)
        
        return self.max_sum