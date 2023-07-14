func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    graph := make(map[int][]int)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        if _, ok := graph[u]; !ok {
            graph[u] = []int{}
        }
        if _, ok := graph[v]; !ok {
            graph[v] = []int{}
        }
        graph[u] = append(graph[u], v)
        graph[v] = append(graph[v], u)
    }
    
    var dfs func(node int, parent int) (int, int)
    dfs = func(node int, parent int) (int, int) {
        profit := 0
        gateCost := 0
        aliceProfit := math.MinInt32
        for _, child := range graph[node] {
            if child == parent {
                continue
            }
            childGateCost, childProfit := dfs(child, node)
            profit += childProfit
            gateCost += childGateCost
            aliceProfit = max(aliceProfit, childProfit)
        }
        if gateCost > amount[node] {
            diff := gateCost - amount[node]
            profit -= 2 * diff
            gateCost -= diff
            aliceProfit = max(aliceProfit-diff, 0)
        } else {
            diff := amount[node] - gateCost
            profit += diff
            aliceProfit += diff
        }
        if node == bob {
            gateCost /= 2
            profit /= 2
            aliceProfit /= 2
            aliceProfit += amount[node]
        }
        return gateCost, max(aliceProfit, 0)
    }
    
    gateCost, aliceProfit := dfs(0, -1)
    return aliceProfit + gateCost
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
