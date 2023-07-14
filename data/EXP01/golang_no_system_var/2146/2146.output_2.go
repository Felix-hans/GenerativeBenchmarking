type Item struct {
    distance, price, row, col int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
    if pq[i].distance != pq[j].distance {
        return pq[i].distance < pq[j].distance
    } else if pq[i].price != pq[j].price {
        return pq[i].price > pq[j].price
    } else if pq[i].row != pq[j].row {
        return pq[i].row < pq[j].row
    } else {
        return pq[i].col < pq[j].col
    }
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
    item := x.(*Item)
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
    n := len(*pq)
    item := (*pq)[n-1]
    *pq = (*pq)[:n-1]
    return item
}

func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
    visited := make([][]bool, len(grid))
    for i := 0; i < len(grid); i++ {
        visited[i] = make([]bool, len(grid[i]))
    }
    
    pq := make(PriorityQueue, 0)
    heap.Init(&pq)
    
    isValid := func(row, col int) bool {
        if row < 0 || row >= len(grid) || col < 0 || col >= len(grid[0]) {
            return false
        }
        price := grid[row][col]
        return price >= pricing[0] && price <= pricing[1]
    }
    
    startItem := &Item{0, grid[start[0]][start[1]], start[0], start[1]}
    heap.Push(&pq, startItem)
    visited[start[0]][start[1]] = true
    
    result := make([][]int, 0)
    
    for len(pq) > 0 && len(result) < k {
        item := heap.Pop(&pq).(*Item)
        result = append(result, []int{item.row, item.col})
        
        neighbors := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
        for _, neighbor := range neighbors {
            newRow, newCol := item.row+neighbor[0], item.col+neighbor[1]
            if isValid(newRow, newCol) && !visited[newRow][newCol] {
                newDistance := item.distance + 1
                newPrice := grid[newRow][newCol]
                newItem := &Item{newDistance, newPrice, newRow, newCol}
                heap.Push(&pq, newItem)
                visited[newRow][newCol] = true
            }
        }
    }
    
    return result
}
