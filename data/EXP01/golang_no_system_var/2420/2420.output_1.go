func goodIndices(nums []int, k int) []int {
    n := len(nums)
    result := []int{}
    
    for i := k; i < n-k; i++ {
        valid := true
        
        for j := i-1; j >= i-k; j-- {
            if nums[j] < nums[j+1] {
                valid = false
                break
            }
        }
        
        for j := i+1; j <= i+k; j++ {
            if nums[j] < nums[j-1] {
                valid = false
                break
            }
        }
        
        if valid {
            result = append(result, i)
        }
    }
    
    return result
}
