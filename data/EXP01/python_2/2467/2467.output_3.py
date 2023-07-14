class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = self.buildGraph(edges)
        visited = set()
        return self.dfs(graph, visited, amount, bob, 0)
    
    def buildGraph(self, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = {}
        for edge in edges:
            node1, node2 = edge
            if node1 not in graph:
                graph[node1] = []
            if node2 not in graph:
                graph[node2] = []
            graph[node1].append(node2)
            graph[node2].append(node1)
        return graph
    
    def dfs(self, graph: Dict[int, List[int]], visited: Set[int], amount: List[int], bob: int, node: int) -> int:
        visited.add(node)
        total_profit = 0
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                gate_cost = abs(amount[neighbor])
                gate_reward = amount[neighbor]
                if neighbor == bob:
                    total_profit += gate_reward // 2
                    amount[neighbor] -= gate_reward // 2
                else:
                    total_profit -= gate_cost // 2
                    amount[neighbor] -= gate_cost // 2
                total_profit += self.dfs(graph, visited, amount, bob, neighbor)
        return total_profit
