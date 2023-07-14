func xorBeauty(nums []int) int {
    n := len(nums)
    xorBeauty := 0
    for i := 0; i < n; i++ {
        for j := 0; j < n; j++ {
            for k := 0; k < n; k++ {
                effectiveValue := (nums[i] | nums[j]) & nums[k]
                xorBeauty ^= effectiveValue
            }
        }
    }
    return xorBeauty
}