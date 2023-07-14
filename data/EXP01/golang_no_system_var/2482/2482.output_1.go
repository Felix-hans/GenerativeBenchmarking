func onesMinusZeros(grid [][]int) [][]int {
    m := len(grid)
    n := len(grid[0])
    
    diff := make([][]int, m)
    for i := 0; i < m; i++ {
        diff[i] = make([]int, n)
    }
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            onesRow := 0
            onesCol := 0
            zerosRow := 0
            zerosCol := 0
            
            for k := 0; k < n; k++ {
                if grid[i][k] == 1 {
                    onesRow++
                } else {
                    zerosRow++
                }
            }
            
            for k := 0; k < m; k++ {
                if grid[k][j] == 1 {
                    onesCol++
                } else {
                    zerosCol++
                }
            }
            
            diff[i][j] = onesRow + onesCol - zerosRow - zerosCol
        }
    }
    
    return diff
}
