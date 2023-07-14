func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    grid := make([][]bool, m)
    for i := 0; i < m; i++ {
        grid[i] = make([]bool, n)
    }
    
    for _, wall := range walls {
        row, col := wall[0], wall[1]
        grid[row][col] = true
    }
    
    for _, guard := range guards {
        row, col := guard[0], guard[1]
        markSeenCells(grid, m, n, row, col)
    }
    
    count := 0
    for _, row := range grid {
        for _, cell := range row {
            if !cell {
                count++
            }
        }
    }
    
    return count
}

func markSeenCells(grid [][]bool, m int, n int, row int, col int) {
    directions := [][]int{{-1, 0}, {0, 1}, {1, 0}, {0, -1}}
    for _, direction := range directions {
        dx, dy := direction[0], direction[1]
        newRow, newCol := row+dx, col+dy
        
        for newRow >= 0 && newRow < m && newCol >= 0 && newCol < n && !grid[newRow][newCol] {
            grid[newRow][newCol] = true
            newRow += dx
            newCol += dy
        }
    }
}
