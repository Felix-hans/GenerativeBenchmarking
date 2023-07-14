To solve this problem, we can create a grid representing the m x n grid and initialize all cells to unguarded. Then, we can iterate through the guards array and mark the cells that can be seen by each guard as guarded. Finally, we can iterate through the walls array and mark the cells with walls as guarded.

Here is the implementation in Go:

```
func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]int, m)
    for i := 0; i < m; i++ {
        grid[i] = make([]int, n)
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            grid[i][j] = 0
        }
    }
    
    for _, guard := range guards {
        x := guard[0]
        y := guard[1]
        
        for i := x - 1; i >= 0; i-- {
            if grid[i][y] == 0 {
                grid[i][y] = 1
            } else {
                break
            }
        }
        
        for j := y + 1; j < n; j++ {
            if grid[x][j] == 0 {
                grid[x][j] = 1
            } else {
                break
            }
        }
        
        for i := x + 1; i < m; i++ {
            if grid[i][y] == 0 {
                grid[i][y] = 1
            } else {
                break
            }
        }
        
        for j := y - 1; j >= 0; j-- {
            if grid[x][j] == 0 {
                grid[x][j] = 1
            } else {
                break
            }
        }
    }
    
    for _, wall := range walls {
        x := wall[0]
        y := wall[1]
        grid[x][y] = 1
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
```