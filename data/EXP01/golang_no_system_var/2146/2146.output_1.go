    "container/heap"
    "math"
)

type Item struct {
    row, col, distance, price int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int { return len(pq) }
func (pq PriorityQueue) Less(i, j int) bool {
    if pq[i].distance == pq[j].distance {
        if pq[i].price == pq[j].price {
            if pq[i].row == pq[j].row {
                return pq[i].col < pq[j].col
            }
            return pq[i].row < pq[j].row
        }
        return pq[i].price < pq[j].price
    }
    return pq[i].distance < pq[j].distance
}
func (pq PriorityQueue) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }

func (pq *PriorityQueue) Push(x interface{}) {
    item := x.(*Item)
    *pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
    old := *pq
    n := len(old)
    item := old[n-1]
    *pq = old[0 : n-1]
    return item
}

func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
    m, n := len(grid), len(grid[0])
    low, high := pricing[0], pricing[1]

    dist := make([]int, m*n)
    prices := make([]int, m*n)
    visited := make([]bool, m*n)
    var pq PriorityQueue

    for i := range dist {
        dist[i] = math.MaxInt32
        prices[i] = math.MaxInt32
    }

    row, col := start[0], start[1]
    dist[row*n+col] = 0
    prices[row*n+col] = 0
    pq = append(pq, &Item{row, col, 0, 0})

    directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

    for pq.Len() > 0 {
        item := heap.Pop(&pq).(*Item)
        row, col := item.row, item.col

        if visited[row*n+col] {
            continue
        }
        visited[row*n+col] = true

        for _, dir := range directions {
            newRow, newCol := row+dir[0], col+dir[1]

            if newRow >= 0 && newRow < m && newCol >= 0 && newCol < n {
                if grid[newRow][newCol] == 0 {
                    continue
                }

                newDist := item.distance + 1
                newPrice := item.price + grid[newRow][newCol]

                if newPrice < low || newPrice > high {
                    continue
                }

                if newDist < dist[newRow*n+newCol] ||
                    (newDist == dist[newRow*n+newCol] && newPrice < prices[newRow*n+newCol]) {
                    dist[newRow*n+newCol] = newDist
                    prices[newRow*n+newCol] = newPrice
                }

                heap.Push(&pq, &Item{newRow, newCol, dist[newRow*n+newCol], prices[newRow*n+newCol]})
            }
        }
    }

    result := make([][]int, 0)
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] > 0 && prices[i*n+j] >= low && prices[i*n+j] <= high {
                result = append(result, []int{i, j})
            }
        }
    }

    sort.Slice(result, func(i, j int) bool {
        if dist[result[i][0]*n+result[i][1]] == dist[result[j][0]*n+result[j][1]] {
            if prices[result[i][0]*n+result[i][1]] == prices[result[j][0]*n+result[j][1]] {
                if result[i][0] == result[j][0] {
                    return result[i][1] < result[j][1]
                }
                return result[i][0] < result[j][0]
            }
            return prices[result[i][0]*n+result[i][1]] < prices[result[j][0]*n+result[j][1]]
        }
        return dist[result[i][0]*n+result[i][1]] < dist[result[j][0]*n+result[j][1]]
    })

    if k > len(result) {
        return result
    }
    return result[:k]
}
