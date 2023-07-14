func isPossibleToCutPath(grid [][]int) bool {
    m := len(grid)
    n := len(grid[0])
  
    if !hasPath(grid, 0, 0, m-1, n-1) {
        return true
    }
  
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            temp := grid[i][j]
            grid[i][j] ^= 1
  
            if !hasPath(grid, 0, 0, m-1, n-1) {
                return true
            }
  
            grid[i][j] = temp
        }
    }
  
    return false
}

func hasPath(grid [][]int, r1, c1, r2, c2 int) bool {
    if grid[r1][c1] == 0 || grid[r2][c2] == 0 {
        return false
    }
  
    m := len(grid)
    n := len(grid[0])
  
    visited := make([]bool, m*n)
    queue := []int{r1*n + c1}
    visited[r1*n+c1] = true
  
    for len(queue) > 0 {
        size := len(queue)
  
        for i := 0; i < size; i++ {
            curr := queue[i]
            r := curr / n
            c := curr % n
  
            if r == r2 && c == c2 {
                return true
            }
  
            if r < m-1 && grid[r+1][c] == 1 && !visited[(r+1)*n+c] {
                queue = append(queue, (r+1)*n+c)
                visited[(r+1)*n+c] = true
            }
  
            if c < n-1 && grid[r][c+1] == 1 && !visited[r*n+c+1] {
                queue = append(queue, r*n+c+1)
                visited[r*n+c+1] = true
            }
        }
  
        queue = queue[size:]
    }
  
    return false
}
