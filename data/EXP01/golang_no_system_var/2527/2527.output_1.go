func xorBeauty(nums []int) int {
    n := len(nums)
    result := 0
    
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            for k := 0; k < n; k++ {
                effectiveValue := (nums[i] | nums[j]) & nums[k]
                result ^= effectiveValue
            }
        }
    }
    
    return result
}
