func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    n := len(amount)
    
    adjList := make([][]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adjList[u] = append(adjList[u], v)
        adjList[v] = append(adjList[v], u)
    }
    
    visited := make([]bool, n)
    res := make([]int, n)
    
    dfs(0, adjList, visited, amount, res)
    
    return res[bob]
}

func dfs(node int, adjList [][]int, visited []bool, amount []int, res []int) {
    visited[node] = true
    result := 0
    
    for _, neighbor := range adjList[node] {
        if !visited[neighbor] {
            dfs(neighbor, adjList, visited, amount, res)
            result = max(result, res[neighbor])
        }
    }
    
    res[node] = result + amount[node]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
