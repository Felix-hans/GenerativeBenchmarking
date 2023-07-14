    "math"
)

func isPossibleToCutPath(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
    
    if !hasPath(grid, 0, 0, m-1, n-1) {
        return true
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                grid[i][j] = 0
                
                if !hasPath(grid, 0, 0, m-1, n-1) {
                    return true
                }
                
                grid[i][j] = 1
            }
        }
    }
    
    return false
}

func hasPath(grid [][]int, startX, startY, endX, endY int) bool {
    m := len(grid)
    n := len(grid[0])
    
    visited := make([][]bool, m)
    for i := 0; i < m; i++ {
        visited[i] = make([]bool, n)
    }
    
    queue := [][]int{{startX, startY}}
    visited[startX][startY] = true
    
    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]
        
        x := curr[0]
        y := curr[1]
        
        if x == endX && y == endY {
            return true
        }
        
        if y+1 < n && grid[x][y+1] == 1 && !visited[x][y+1] {
            queue = append(queue, []int{x, y+1})
            visited[x][y+1] = true
        }
        
        if x+1 < m && grid[x+1][y] == 1 && !visited[x+1][y] {
            queue = append(queue, []int{x+1, y})
            visited[x+1][y] = true
        }
    }
    
    return false
}