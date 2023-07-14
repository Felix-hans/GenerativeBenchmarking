type Node struct {
    id     int
    parent int
    child  []int
}

func mostProfitablePath(edges [][]int, bob int, amount []int) int {
    n := len(amount)
    nodes := make([]Node, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        nodes[u].child = append(nodes[u].child, v)
        nodes[v].parent = u
    }

    dfs(&nodes, bob, amount, math.MinInt64)
    return nodes[bob].profit
}

func dfs(nodes *[]Node, curr int, amount []int, maxProfit int) {
    node := &((*nodes)[curr])
    gate := amount[curr]
    node.profit = gate

    for _, child := range node.child {
        dfs(nodes, child, amount, maxProfit)
        node.profit += (*nodes)[child].profit
    }

    if node.parent != 0 {
        gate /= 2
        (*nodes)[node.parent].profit += gate
        node.profit += gate - amount[node.parent]
    }

    if node.profit > maxProfit {
        maxProfit = node.profit
    }
}
