func validPartition(nums []int) bool {
    n := len(nums)
    if n < 3 {
        return false
    }
    
    prev, count := nums[0], 1
    
    for i := 1; i < n; i++ {
        if nums[i] == prev {
            count++
        } else {
            if count > 2 {
                return true
            }
            prev = nums[i]
            count = 1
        }
    }
    
    return count > 2
}
