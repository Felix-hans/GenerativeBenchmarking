type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func maxStarSum(vals []int, edges [][]int, k int) int {
	graph := make(map[int][]int)
	for _, edge := range edges {
		node1, node2 := edge[0], edge[1]
		graph[node1] = append(graph[node1], node2)
		graph[node2] = append(graph[node2], node1)
	}

	maxSum := 0
	heap := &MinHeap{}

	for i := 0; i < len(vals); i++ {
		currentSum := vals[i]
		for _, neighbor := range graph[i] {
			currentSum += vals[neighbor]
		}

		if heap.Len() < k {
			heap.Push(currentSum)
		} else if currentSum > heap[0] {
			heap.Pop()
			heap.Push(currentSum)
		}

		if currentSum > maxSum {
			maxSum = currentSum
		}
	}

	for heap.Len() > 0 {
		maxSum += heap.Pop().(int)
	}

	return maxSum
}
