func isGuarded(row, col int, guards [][]int, walls [][]int) bool {
    for _, guard := range guards {
        if guard[0] == row && guard[1] == col {
            return true
        }
    }

    for _, wall := range walls {
        wallRow, wallCol := wall[0], wall[1]
        if wallRow == row && wallCol == col {
            return true
        }
    }

    return false
}

func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
    unguarded := 0

    for row := 0; row < m; row++ {
        for col := 0; col < n; col++ {
            isUnguarded := true

            if isGuarded(row, col, guards, walls) {
                isUnguarded = false
            } else {
                if row > 0 && isGuarded(row-1, col, guards, walls) {
                    isUnguarded = false
                }
                if col < n-1 && isGuarded(row, col+1, guards, walls) {
                    isUnguarded = false
                }
                if row < m-1 && isGuarded(row+1, col, guards, walls) {
                    isUnguarded = false
                }
                if col > 0 && isGuarded(row, col-1, guards, walls) {
                    isUnguarded = false
                }
            }

            if isUnguarded {
                unguarded++
            }
        }
    }

    return unguarded
}
