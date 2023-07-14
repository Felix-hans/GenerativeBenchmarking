func equalPairs(grid [][]int) int {
    count := 0

    rows := make(map[string]int)
    cols := make(map[string]int)

    n := len(grid)

    for i := 0; i < n; i++ {
        rowStr := ""
        colStr := ""

        for j := 0; j < n; j++ {
            rowStr += strconv.Itoa(grid[i][j]) + ","
            colStr += strconv.Itoa(grid[j][i]) + ","
        }

        rows[rowStr]++
        cols[colStr]++
    }

    for _, val := range rows {
        count += (val * (val - 1)) / 2
    }

    for _, val := range cols {
        count += (val * (val - 1)) / 2
    }

    return count
}
