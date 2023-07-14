Here is the implementation of the given task:

```
type ListNode struct {
	Val  int
	Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
	matrix := make([][]int, m)
	for i := 0; i < m; i++ {
		matrix[i] = make([]int, n)
		for j := 0; j < n; j++ {
			matrix[i][j] = -1
		}
	}

	rowStart, rowEnd := 0, m-1
	colStart, colEnd := 0, n-1
	direction := 0

	curr := head
	for rowStart <= rowEnd && colStart <= colEnd && curr != nil {
		if direction == 0 {
			for j := colStart; j <= colEnd; j++ {
				matrix[rowStart][j] = curr.Val
				curr = curr.Next
			}
			rowStart++
		} else if direction == 1 {
			for i := rowStart; i <= rowEnd; i++ {
				matrix[i][colEnd] = curr.Val
				curr = curr.Next
			}
			colEnd--
		} else if direction == 2 {
			for j := colEnd; j >= colStart; j-- {
				matrix[rowEnd][j] = curr.Val
				curr = curr.Next
			}
			rowEnd--
		} else if direction == 3 {
			for i := rowEnd; i >= rowStart; i-- {
				matrix[i][colStart] = curr.Val
				curr = curr.Next
			}
			colStart++
		}
		direction = (direction + 1) % 4
	}

	return matrix
}
```

Explanation:
- We create a matrix of size m x n with all values set to -1.
- We use four variables (rowStart, rowEnd, colStart, colEnd) to keep track of the boundaries of the matrix.
- We use a direction variable to determine the direction in which we need to fill the matrix (0: right, 1: down, 2: left, 3: up).
- We iterate through the matrix in a spiral order and fill each cell with the corresponding value from the linked list.
- Finally, we return the generated matrix.