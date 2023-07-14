func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]int, m)
    for i := 0; i < m; i++ {
        grid[i] = make([]int, n)
    }
    
    for _, guard := range guards {
        row, col := guard[0], guard[1]
        grid[row][col] = -1
    }
    for _, wall := range walls {
        row, col := wall[0], wall[1]
        grid[row][col] = -2
    }
    
    unguarded := 0
    directions := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
    
    var dfs func(row, col int)
    dfs = func(row, col int) {
        if row < 0 || row >= m || col < 0 || col >= n {
            return
        }
        if grid[row][col] == -1 || grid[row][col] == -2 {
            return
        }
        if grid[row][col] == 0 {
            unguarded++
        }
        grid[row][col] = -1 // mark as visited
        for _, direction := range directions {
            newRow, newCol := row+direction[0], col+direction[1]
            dfs(newRow, newCol)
        }
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                dfs(i, j)
            }
        }
    }
    
    return unguarded
}
