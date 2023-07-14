func halveArray(nums []int) int {
    sum := 0
    for _, num := range nums {
        sum += num
    }

    target := sum / 2
    maxNum := max(nums)

    for target > 0 {
        if maxNum%2 == 1 {
            target -= maxNum / 2
            maxNum /= 2
        } else {
            diff := target - maxNum/2
            if diff >= 0 {
                target -= maxNum / 2
                maxNum /= 2
            } else {
                maxNum /= 2
            }
        }
    }

    operations := 0
    for _, num := range nums {
        operations += countOperations(num)
    }

    return operations
}

func max(nums []int) int {
    maxNum := nums[0]
    for i := 1; i < len(nums); i++ {
        if nums[i] > maxNum {
            maxNum = nums[i]
        }
    }
    return maxNum
}

func countOperations(num int) int {
    operations := 0
    for num > 0 && num%2 == 0 {
        num /= 2
        operations++
    }
    return operations
}
