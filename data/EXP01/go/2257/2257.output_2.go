func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]int, m)
    for i := 0; i < m; i++ {
        grid[i] = make([]int, n)
    }
    
    for _, wall := range walls {
        row, col := wall[0], wall[1]
        grid[row][col] = -1
    }
    
    for _, guard := range guards {
        queue := make([][]int, 0)
        queue = append(queue, guard)
        directions := [][]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
        
        for len(queue) > 0 {
            curr := queue[0]
            queue = queue[1:]
            row, col := curr[0], curr[1]
            
            if row < 0 || row >= m || col < 0 || col >= n || grid[row][col] == -1 || grid[row][col] == 1 {
                continue
            }
            
            grid[row][col] = 1
            
            for _, dir := range directions {
                newRow, newCol := row+dir[0], col+dir[1]
                queue = append(queue, []int{newRow, newCol})
            }
        }
    }
    
    count := 0
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 0 {
                count++
            }
        }
    }
    
    return count
}
