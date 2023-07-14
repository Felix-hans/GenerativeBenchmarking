        class Solution:
            def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
                graph = [[] for _ in range(len(amount))]
                for edge in edges:
                    graph[edge[0]].append(edge[1])
                    graph[edge[1]].append(edge[0])
                
                def dfs(node, parent):
                    max_profit = amount[node]
                    for neighbor in graph[node]:
                        if neighbor != parent:
                            profit = dfs(neighbor, node)
                            max_profit += max(0, profit)
                    return max_profit
                
                return dfs(bob, -1)
        