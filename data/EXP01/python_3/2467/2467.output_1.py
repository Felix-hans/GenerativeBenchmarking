# @lc app=leetcode id=2467 lang=python
class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        net_income = [0] * n

        def dfs(node, parent):
            for child in graph[node]:
                if child == parent:
                    continue
                dfs(child, node)
                net_income[node] += max(net_income[child], -amount[child])

        dfs(bob, -1)
        return amount[bob] + net_income[bob]