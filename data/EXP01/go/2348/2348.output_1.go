func zeroFilledSubarray(nums []int) int64 {
    count := int64(0)
    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            count += int64(subarrayCount(nums[i+1:]))
        }
    }
    return count
}

func subarrayCount(nums []int) int {
    count := 0
    for i := 0; i < len(nums); i++ {
        if nums[i] != 0 {
            break
        }
        count++
    }
    return count
}
