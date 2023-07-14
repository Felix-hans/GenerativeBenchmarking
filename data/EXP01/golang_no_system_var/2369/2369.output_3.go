func validPartition(nums []int) bool {
    n := len(nums)
    
    for i := 0; i < n-1; i++ {
        if nums[i] == nums[i+1] {
            return true
        }
    }
    
    for i := 0; i < n-2; i++ {
        if nums[i] == nums[i+2] {
            return true
        }
    }
    
    for i := 0; i < n-2; i++ {
        if nums[i+1] == nums[i]+1 && nums[i+2] == nums[i]+2 {
            return true
        }
    }
    
    return false
}
