func goodIndices(nums []int, k int) []int {
    n := len(nums)

    var result []int

    for i := k; i < n-k; i++ {
        good := true

        for j := i-k; j < i; j++ {
            if nums[j] < nums[j+1] {
                good = false
                break
            }
        }

        for j := i; j < i+k; j++ {
            if nums[j] > nums[j+1] {
                good = false
                break
            }
        }

        if good {
            result = append(result, i)
        }
    }

    return result
}
