func goodIndices(nums []int, k int) []int {
    result := make([]int, 0)

    for i := k; i < len(nums)-k; i++ {
        nonIncreasing := true
        for j := i-1; j >= i-k; j-- {
            if nums[j] < nums[j+1] {
                nonIncreasing = false
                break
            }
        }

        nonDecreasing := true
        for j := i+1; j <= i+k; j++ {
            if nums[j] < nums[j-1] {
                nonDecreasing = false
                break
            }
        }

        if nonIncreasing && nonDecreasing {
            result = append(result, i)
        }
    }

    return result
}
