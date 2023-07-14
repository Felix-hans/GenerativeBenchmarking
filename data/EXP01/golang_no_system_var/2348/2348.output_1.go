func zeroFilledSubarray(nums []int) int {
    numZeros := 0
    result := 0
    
    for i := 0; i < len(nums); i++ {
        if nums[i] == 0 {
            numZeros++
        } else {
            result += (numZeros * (numZeros + 1)) / 2
            numZeros = 0
        }
    }
    
    result += (numZeros * (numZeros + 1)) / 2
    
    return result
}
