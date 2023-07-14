func zeroFilledSubarray(nums []int) int {
    count := 0
    result := 0
    
    for _, num := range nums {
        if num == 0 {
            count++
        } else {
            count = 0
        }
        
        result += count
    }
    
    return result
}
