func buildGraph(vals []int, edges [][]int) map[int][]int {
    graph := make(map[int][]int)
    
    for _, edge := range edges {
        x, y := edge[0], edge[1]
        graph[x] = append(graph[x], y)
        graph[y] = append(graph[y], x)
    }
    
    return graph
}

func dfs(node, parent int, graph map[int][]int, vals []int, k int, sum int, maxSum *int) {
    sum += vals[node]
    neighbors := graph[node]
    count := len(neighbors) - 1 // exclude parent node
    
    for _, neighbor := range neighbors {
        if neighbor != parent {
            dfs(neighbor, node, graph, vals, k, sum, maxSum)
        }
    }
    
    if count <= k {
        *maxSum = max(*maxSum, sum)
    }
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

func maxStarSum(vals []int, edges [][]int, k int) int {
    graph := buildGraph(vals, edges)
    maxSum := 0
    
    dfs(0, -1, graph, vals, k, 0, &maxSum)
    
    return maxSum
}
