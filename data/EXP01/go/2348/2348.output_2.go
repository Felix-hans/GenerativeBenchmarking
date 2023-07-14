func zeroFilledSubarray(nums []int) int64 {
    count := int64(0)
    length := len(nums)
    for i := 0; i < length; i++ {
        if nums[i] == 0 {
            count++
        }
        for j := i + 1; j < length; j++ {
            if nums[j] == 0 {
                count++
            } else {
                break
            }
        }
    }
    return count
}
