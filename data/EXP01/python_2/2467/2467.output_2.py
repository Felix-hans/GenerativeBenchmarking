class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)  # Adjacency list representation of the tree
        
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)
        
        return self.dfs(graph, bob, amount, 0, bob)
    
    def dfs(self, graph, bob, amount, node, parent):
        net_income = 0  # Net income at the current node
        
        if len(graph[node]) == 1 and node != bob:
            return max(0, amount[node])  # Return the cash reward if it's positive, else 0
        
        for adj_node in graph[node]:
            if adj_node != parent:
                adj_income = self.dfs(graph, bob, amount, adj_node, node)
                
                gate_value = amount[node] // 2
                
                if adj_node == bob:
                    adj_income += gate_value
                elif node == bob:
                    adj_income -= gate_value
                
                net_income = max(net_income, adj_income)
        
        return net_income
