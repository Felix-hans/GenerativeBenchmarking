func maxStarSum(vals []int, edges [][]int, k int) int {
    n := len(vals)
    graph := make(map[int][]int)
    for _, edge := range edges {
        a, b := edge[0], edge[1]
        graph[a] = append(graph[a], b)
        graph[b] = append(graph[b], a)
    }
    
    maxSum := vals[0] // initialize maxSum with the value of the first node
    
    var dfs func(int, int, int) int
    dfs = func(node, parent, edgesUsed int) int {
        sum := vals[node]
        children := 0
        
        for _, neighbor := range graph[node] {
            if neighbor != parent {
                childSum := dfs(neighbor, node, edgesUsed+1)
                if childSum > 0 {
                    sum += childSum
                    children++
                }
            }
        }
        
        if children == 0 && edgesUsed <= k {
            return sum
        }
        
        if edgesUsed < k && sum > maxSum {
            maxSum = sum
        }
        
        return sum
    }
    
    dfs(0, -1, 0) // start DFS from the first node
    
    return maxSum
}
