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

    dir := 0 // 0: right, 1: down, 2: left, 3: up
    top, bottom, left, right := 0, m-1, 0, n-1
    row, col := 0, 0
    node := head
    count := 0
    for node != nil {
        matrix[row][col] = node.Val
        node = node.Next
        count++

        switch dir {
        case 0: // right
            col++
            if col > right {
                dir = 1
                top++
                col = right
            }
        case 1: // down
            row++
            if row > bottom {
                dir = 2
                right--
                row = bottom
            }
        case 2: // left
            col--
            if col < left {
                dir = 3
                bottom--
                col = left
            }
        case 3: // up
            row--
            if row < top {
                dir = 0
                left++
                row = top
            }
        }
    }

    return matrix
}
