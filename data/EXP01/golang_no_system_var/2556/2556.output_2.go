    "container/list"
)

func isPossibleToCutPath(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
    
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }
    
    queue := list.New()
    queue.PushBack([]int{0, 0})
    
    for queue.Len() > 0 {
        pos := queue.Remove(queue.Front()).([]int)
        row := pos[0]
        col := pos[1]
        
        visited[row][col] = true
        
        if row == m-1 && col == n-1 {
            if grid[0][0] == grid[m-1][n-1] {
                return true
            }
            
            return findPath(grid, visited, m, n, row, col, -1, -1)
        }
        
        if row+1 < m && grid[row+1][col] == 1 && !visited[row+1][col] {
            queue.PushBack([]int{row+1, col})
        }
        
        if col+1 < n && grid[row][col+1] == 1 && !visited[row][col+1] {
            queue.PushBack([]int{row, col+1})
        }
    }
    
    return false
}

func findPath(grid [][]int, visited [][]bool, m, n, row, col, flipRow, flipCol int) bool {
    
    if flipRow >= 0 && flipCol >= 0 {
        grid[flipRow][flipCol] = 0
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            visited[i][j] = false
        }
    }
    
    queue := list.New()
    queue.PushBack([]int{row, col})
    
    for queue.Len() > 0 {
        pos := queue.Remove(queue.Front()).([]int)
        row := pos[0]
        col := pos[1]
        
        visited[row][col] = true
        
        if row == m-1 && col == n-1 {
            return true
        }
        
        if row+1 < m && grid[row+1][col] == 1 && !visited[row+1][col] {
            queue.PushBack([]int{row+1, col})
        }
        
        if col+1 < n && grid[row][col+1] == 1 && !visited[row][col+1] {
            queue.PushBack([]int{row, col+1})
        }
    }
    
    return false
}