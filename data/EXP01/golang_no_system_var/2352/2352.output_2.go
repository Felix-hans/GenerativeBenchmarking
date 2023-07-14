func equalPairs(grid [][]int) int {
    n := len(grid)
    count := 0

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            if isEqual(grid[i], getColumn(grid, j)) {
                count++
            }
        }
    }

    return count
}

func getColumn(grid [][]int, col int) []int {
    n := len(grid)
    column := make([]int, n)

    for i := 0; i < n; i++ {
        column[i] = grid[i][col]
    }

    return column
}

func isEqual(arr1, arr2 []int) bool {
    if len(arr1) != len(arr2) {
        return false
    }

    for i := 0; i < len(arr1); i++ {
        if arr1[i] != arr2[i] {
            return false
        }
    }

    return true
}
