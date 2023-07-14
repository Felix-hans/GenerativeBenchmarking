func zeroFilledSubarray(nums []int) int {
    count := 0
    prefixSum := make(map[int]int)
    prefixSum[0] = 1
    sum := 0
    
    for _, num := range nums {
        if num == 0 {
            sum += 1
        } else {
            sum -= 1
        }
        
        if freq, exist := prefixSum[sum]; exist {
            count += freq
        }
        prefixSum[sum] += 1
    }
    
    return count
}
