type ListNode struct {
    Val  int
    Next *ListNode
}

func spiralMatrix(m int, n int, head *ListNode) [][]int {
    matrix := make([][]int, m)
    for i := range matrix {
        matrix[i] = make([]int, n)
    }

    nums := make([]int, 0)
    curr := head
    for curr != nil {
        nums = append(nums, curr.Val)
        curr = curr.Next
    }

    left, right := 0, n-1
    top, bottom := 0, m-1
    index := 0

    for left <= right && top <= bottom {
        for j := left; j <= right; j++ {
            if index < len(nums) {
                matrix[top][j] = nums[index]
                index++
            } else {
                matrix[top][j] = -1
            }
        }
        top++

        for i := top; i <= bottom; i++ {
            if index < len(nums) {
                matrix[i][right] = nums[index]
                index++
            } else {
                matrix[i][right] = -1
            }
        }
        right--

        if top <= bottom {
            for j := right; j >= left; j-- {
                if index < len(nums) {
                    matrix[bottom][j] = nums[index]
                    index++
                } else {
                    matrix[bottom][j] = -1
                }
            }
            bottom--
        }
        
        if left <= right {
            for i := bottom; i >= top; i-- {
                if index < len(nums) {
                    matrix[i][left] = nums[index]
                    index++
                } else {
                    matrix[i][left] = -1
                }
            }
            left++
        }
    }
    
    return matrix
}

,
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    m, n := 3, 5
    result := spiralMatrix(m, n, head)
    for _, row := range result {
        fmt.Println(row)
    }
}
