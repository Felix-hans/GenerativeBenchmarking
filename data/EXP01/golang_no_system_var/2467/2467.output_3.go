func dfs(node, prev int, isBob bool, edges [][]int, amount []int) int {
    if len(edges[node]) == 1 {
        return amount[node]
    }
    
    maxIncome := 0
    for _, next := range edges[node] {
        if next == prev {
            continue
        }
        
        income := amount[node] + dfs(next, node, !isBob, edges, amount)
        if !isBob {
            maxIncome = max(maxIncome, income)
        } else {
            maxIncome = min(maxIncome, -income)
        }
    }
    
    return maxIncome
}

func maxProfitablePath(edges [][]int, bob int, amount []int) int {
    n := len(amount)
    
    adj := make([][]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }
    
    return dfs(0, -1, false, adj, amount)
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
