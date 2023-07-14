func zeroFilledSubarray(nums []int) int64 {
    count := int64(0)
    zeroCount := 0
    zeroMap := make(map[int]int64)

    for _, num := range nums {
        if num == 0 {
            zeroCount++
        } else {
            count += int64(zeroCount*(zeroCount+1)/2) // Calculate the number of subarrays formed by zeros
            zeroCount = 0
        }
        count += zeroMap[zeroCount] // Add the count of subarrays with the current zero count
        zeroMap[zeroCount]++ // Increment the count of subarrays with the current zero count
    }

    count += int64(zeroCount*(zeroCount+1)/2) // Calculate the number of subarrays formed by zeros at the end
    return count
}
