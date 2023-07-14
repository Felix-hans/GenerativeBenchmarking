func isPossibleToCutPath(grid [][]int) bool {
	m := len(grid)
	n := len(grid[0])
	visited := make([][]bool, m)
	for i := 0; i < m; i++ {
		visited[i] = make([]bool, n)
	}

	if dfs(grid, 0, 0, visited) {
		return true
	}

	return false
}

func dfs(grid [][]int, row, col int, visited [][]bool) bool {
	m := len(grid)
	n := len(grid[0])
	if row == m-1 && col == n-1 {
		return true
	}

	if row >= m || col >= n || visited[row][col] || grid[row][col] == 0 {
		return false
	}

	if row+1 < m && col+1 < n && grid[row+1][col] == 0 && grid[row][col+1] == 0 {
	return true
	}

	visited[row][col] = true

	if row+1 < m && dfs(grid, row+1, col, visited) {
		return true
	}

	if col+1 < n && dfs(grid, row, col+1, visited) {
		return true
	}

	return false
}
