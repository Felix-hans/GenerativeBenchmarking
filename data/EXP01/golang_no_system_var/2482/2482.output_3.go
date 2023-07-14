func onesMinusZeros(grid [][]int) [][]int {
    m := len(grid)
    n := len(grid[0])
    
    onesRow := make([]int, m)
    onesCol := make([]int, n)
    zerosRow := make([]int, m)
    zerosCol := make([]int, n)
    
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if grid[i][j] == 1 {
                onesRow[i]++
                onesCol[j]++
            } else {
                zerosRow[i]++
                zerosCol[j]++
            }
        }
    }
    
    diff := make([][]int, m)
    for i := 0; i < m; i++ {
        diff[i] = make([]int, n)
        for j := 0; j < n; j++ {
            diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        }
    }
    
    return diff
}
