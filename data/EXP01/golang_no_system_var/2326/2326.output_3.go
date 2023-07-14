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
    
    row := 0
    col := 0
    direction := 0 // 0 = right, 1 = down, 2 = left, 3 = up
    
    for head != nil {
        matrix[row][col] = head.Val
        head = head.Next
        
        if direction == 0 {
            col++
            if col == n || matrix[row][col] != -1 {
                col--
                direction = 1
                row++
            }
        } else if direction == 1 {
            row++
            if row == m || matrix[row][col] != -1 {
                row--
                direction = 2
                col--
            }
        } else if direction == 2 {
            col--
            if col < 0 || matrix[row][col] != -1 {
                col++
                direction = 3
                row--
            }
        } else if direction == 3 {
            row--
            if row < 0 || matrix[row][col] != -1 {
                row++
                direction = 0
                col++
            }
        }
    }
    
    return matrix
}
