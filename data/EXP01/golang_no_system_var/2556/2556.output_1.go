func isPossibleToCutPath(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
    
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }
    
    var dfs func(row, col int) bool
    dfs = func(row, col int) bool {
        visited[row][col] = true
        
        if row == m-1 && col == n-1 {
            return true
        }
        
        if row+1 < m && grid[row+1][col] == 1 && !visited[row+1][col] {
            if dfs(row+1, col) {
                return true
            }
        }
        
        if col+1 < n && grid[row][col+1] == 1 && !visited[row][col+1] {
            if dfs(row, col+1) {
                return true
            }
        }
        
        return false
    }
    
    if dfs(0, 0) {
        return false
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            grid[i][j] = 1 - grid[i][j]
            
            for k := 0; k < m; k++ {
                for l := 0; l < n; l++ {
                    visited[k][l] = false
                }
            }
            
            if !dfs(0, 0) {
                return true
            }
            
            grid[i][j] = 1 - grid[i][j]
        }
    }
    
    return false
}

,{1,0,0},{1,1,1}}
    fmt.Println(isPossibleToCutPath(grid1)) // Output: true
    
    grid2 := [][]int{{1,1,1},{1,0,1},{1,1,1}}
    fmt.Println(isPossibleToCutPath(grid2)) // Output: false
}