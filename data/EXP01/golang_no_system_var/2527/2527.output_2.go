func xorBeauty(nums []int) int {
    n := len(nums)
    beauty := 0

    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            for k := 0; k < n; k++ {
                effective := (nums[i] | nums[j]) & nums[k]
                beauty ^= effective
            }
        }
    }

    return beauty
}
