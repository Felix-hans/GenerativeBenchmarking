To solve this problem, we can use a set to keep track of the positions of the guards and walls. We will iterate through the guards and walls arrays and add their positions to the set. Then we will iterate through all the cells in the grid and check if each cell is guarded or not. If a cell is not guarded, we will increment a count variable. Finally, we will return the count variable.

Here's the implementation in Go:

```
func countUnguarded(m int, n int, guards [][]int, walls [][]int) int {
	guardsSet := make(map[[2]int]bool)
	for _, guard := range guards {
		guardsSet[[2]int{guard[0], guard[1]}] = true
	}
	for _, wall := range walls {
		guardsSet[[2]int{wall[0], wall[1]}] = true
	}

	count := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if !isGuarded(i, j, guardsSet) {
				count++
			}
		}
	}

	return count
}

func isGuarded(row, col int, guardsSet map[[2]int]bool) bool {
	for guard := range guardsSet {
		if guard[0] == row || guard[1] == col {
			return true
		}
	}

	for guard := range guardsSet {
		if abs(guard[0]-row) == abs(guard[1]-col) {
			return true
		}
	}

	return false
}

func abs(num int) int {
	if num < 0 {
		return -num
	}
	return num
}
```

The `countUnguarded` function takes the dimensions of the grid (`m` and `n`), the positions of the guards, and the positions of the walls as input. It creates a set (`guardsSet`) to store the positions of the guards and walls. It then iterates through all the cells in the grid and checks if each cell is guarded or not using the `isGuarded` function. If a cell is not guarded, it increments the `count` variable. Finally, it returns the `count` variable.

The `isGuarded` function takes the row and column indices of a cell and the `guardsSet` set as input. It checks if any guard is in the same row or column as the cell or on the diagonal of the cell. If a guard is found in any of these positions, it returns `true`, indicating that the cell is guarded. Otherwise, it returns `false`.

The `abs` function calculates the absolute value of a number `num`.