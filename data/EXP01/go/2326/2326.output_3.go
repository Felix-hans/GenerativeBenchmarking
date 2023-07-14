type ListNode struct {
    Val  int
    Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    matrix := make([][]int, m)
    for i := 0; i < m; i++ {
        matrix[i] = make([]int, n)
        for j := 0; j < n; j++ {
            if head != nil {
                matrix[i][j] = head.Val
                head = head.Next
            } else {
                matrix[i][j] = -1
            }
        }
    }
    return matrix
}

}}}}}}}}}}}}}
    m, n := 3, 5
    result := spiralMatrix(m, n, head)
    for i := 0; i < m; i++ {
        fmt.Println(result[i])
    }
}
