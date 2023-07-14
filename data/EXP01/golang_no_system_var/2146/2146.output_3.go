	"container/heap"
	"math"
)

type Item struct {
	row, col int
	price    int
	distance int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
	return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
	if pq[i].distance != pq[j].distance {
		return pq[i].distance < pq[j].distance
	}
	if pq[i].price != pq[j].price {
		return pq[i].price > pq[j].price
	}
	if pq[i].row != pq[j].row {
		return pq[i].row < pq[j].row
	}
	return pq[i].col < pq[j].col
}

func (pq PriorityQueue) Swap(i, j int) {
	pq[i], pq[j] = pq[j], pq[i]
	pq[i].distance, pq[j].distance = pq[j].distance, pq[i].distance
}

func (pq *PriorityQueue) Push(x interface{}) {
	item := x.(*Item)
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	*pq = old[:n-1]
	return item
}

func shortestPath(grid [][]int, start []int) []int {
	m := len(grid)
	n := len(grid[0])
	distance := make([][]int, m)
	for i := range distance {
		distance[i] = make([]int, n)
		for j := range distance[i] {
			distance[i][j] = math.MaxInt32
		}
	}
	distance[start[0]][start[1]] = 0

	pq := make(PriorityQueue, 0)
	heap.Push(&pq, &Item{start[0], start[1], grid[start[0]][start[1]], 0})

	directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}

	for pq.Len() > 0 {
		item := heap.Pop(&pq).(*Item)
		row, col := item.row, item.col

		if distance[row][col] < item.distance {
			continue
		}

		for _, dir := range directions {
			newRow, newCol := row+dir[0], col+dir[1]
			if newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && grid[newRow][newCol] != 0 {
				newDistance := distance[row][col] + 1
				if newDistance < distance[newRow][newCol] {
					distance[newRow][newCol] = newDistance
					heap.Push(&pq, &Item{newRow, newCol, grid[newRow][newCol], newDistance})
				}
			}
		}
	}

	return distance
}

func highestRankedKItems(grid [][]int, pricing []int, start []int, k int) [][]int {
	m := len(grid)
	n := len(grid[0])

	distance := shortestPath(grid, start)

	result := make([][]int, 0)
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			price := grid[row][col]
			if price >= pricing[0] && price <= pricing[1] {
				result = append(result, []int{row, col})
			}
		}
	}

	sort.Slice(result, func(i, j int) bool {
		if distance[result[i][0]][result[i][1]] != distance[result[j][0]][result[j][1]] {
			return distance[result[i][0]][result[i][1]] < distance[result[j][0]][result[j][1]]
		}
		if grid[result[i][0]][result[i][1]] != grid[result[j][0]][result[j][1]] {
			return grid[result[i][0]][result[i][1]] < grid[result[j][0]][result[j][1]]
		}
		if result[i][0] != result[j][0] {
			return result[i][0] < result[j][0]
		}
		return result[i][1] < result[j][1]
	})

	if k > len(result) {
		return result
	}
	return result[:k]
}
