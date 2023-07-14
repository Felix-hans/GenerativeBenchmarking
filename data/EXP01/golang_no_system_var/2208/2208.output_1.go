func halveArray(nums []int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(nums)))
    
    sum := 0
    for _, num := range nums {
        sum += num
    }
    
    target := sum / 2
    
    count := 0
    currentSum := 0
    for _, num := range nums {
        currentSum += num
        count++
        if currentSum >= target {
            break
        }
    }
    
    return count
}
