func dfs(v int, edges [][]int, bob int, amount []int, dp []int) int {
    if dp[v] != math.MinInt64 {
        return dp[v]
    }
    
    if v == 0 {
        dp[v] = amount[0]
        return dp[v]
    }
    
    n := len(edges)
    total := amount[v]
    count := 1
    
    for i := 0; i < n; i++ {
        if edges[i][1] == v {
            child := edges[i][0]
            
            if child == bob {
                continue
            }
            
            profit := dfs(child, edges, bob, amount, dp)
            
            if profit > 0 {
                total += profit
                count++
            }
            
            dp[v] = max(dp[v], profit)
        }
    }
    
    if count > 1 && (count%2 == 0) {
        total -= total / 2
    }
    
    dp[v] = max(dp[v], total)
    return dp[v]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    n := len(amount)
    dp := make([]int, n)
    
    for i := 0; i < n; i++ {
        dp[i] = math.MinInt64
    }
    
    dfs(0, edges, bob, amount, dp)
    return dp[0]
}
