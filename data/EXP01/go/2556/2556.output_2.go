func isPossibleToCutPath(grid [][]int) bool {
    m := len(grid)
    if m == 0 {
        return false
    }
    n := len(grid[0])
    if n == 0 {
        return false
    }
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }
    if !dfs(grid, &visited, 0, 0) {
        return true
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                grid[i][j] = 0
                visited := make([][]bool, m)
                for i := 0; i < m; i++ {
                    visited[i] = make([]bool, n)
                }
                if !dfs(grid, &visited, 0, 0) {
                    return true
                }
                grid[i][j] = 1
            }
        }
    }

    return false
}

func dfs(grid [][]int, visited *[][]bool, row, col int) bool {
    m := len(grid)
    n := len(grid[0])
    if row == m-1 && col == n-1 {
        return true
    }
    (*visited)[row][col] = true
    if row+1 < m && grid[row+1][col] == 1 && !(*visited)[row+1][col] {
        if dfs(grid, visited, row+1, col) {
            return true
        }
    }
    if col+1 < n && grid[row][col+1] == 1 && !(*visited)[row][col+1] {
        if dfs(grid, visited, row, col+1) {
            return true
        }
    }
    return false
}
