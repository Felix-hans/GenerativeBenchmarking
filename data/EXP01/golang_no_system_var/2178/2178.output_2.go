func maximumEvenSplit(finalSum int64) []int64 {
    
    dp := make([]int64, finalSum+1)
    
    nums := make([][]int64, finalSum+1)
    
    dp[0] = 0
    nums[0] = []int64{}
    
    for i := int64(1); i <= finalSum; i++ {
        maxInt := int64(math.MinInt64)
        maxNums := []int64{}
        
        for j := int64(1); j <= i; j++ {
            if j%2 == 0 && j <= i {
                if dp[i-j] > maxInt {
                    maxInt = dp[i-j]
                    maxNums = make([]int64, len(nums[i-j]))
                    copy(maxNums, nums[i-j])
                }
            }
        }
        
        if maxInt >= 0 {
            dp[i] = maxInt + 1
            nums[i] = append(maxNums, i)
        } else {
            dp[i] = -1
            nums[i] = []int64{}
        }
    }
    
    if dp[finalSum] >= 0 {
        return nums[finalSum]
    }
    return []int64{}
}
