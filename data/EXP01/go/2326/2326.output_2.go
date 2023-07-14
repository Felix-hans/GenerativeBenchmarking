type ListNode struct {
    Val  int
    Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    matrix := make([][]int, m)
    for i := range matrix {
        matrix[i] = make([]int, n)
    }
    
    values := make([]int, 0)
    node := head
    for node != nil {
        values = append(values, node.Val)
        node = node.Next
    }
    
    left, right := 0, n-1
    top, bottom := 0, m-1
    index := 0
    
    for left <= right && top <= bottom {
        for i := left; i <= right && index < len(values); i++ {
            matrix[top][i] = values[index]
            index++
        }
        top++
        
        for i := top; i <= bottom && index < len(values); i++ {
            matrix[i][right] = values[index]
            index++
        }
        right--
        
        for i := right; i >= left && index < len(values); i-- {
            matrix[bottom][i] = values[index]
            index++
        }
        bottom--
        
        for i := bottom; i >= top && index < len(values); i-- {
            matrix[i][left] = values[index]
            index++
        }
        left++
    }
    
    for ; index < len(values); index++ {
        matrix[top][left] = values[index]
        if left < right {
            left++
        } else if top < bottom {
            top++
        }
    }
    
    for i := range matrix {
        for j := range matrix[i] {
            if matrix[i][j] == 0 {
                matrix[i][j] = -1
            }
        }
    }
    
    return matrix
}
