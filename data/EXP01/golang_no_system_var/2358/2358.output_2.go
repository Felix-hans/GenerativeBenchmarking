func maximumGroups(grades []int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(grades))) // Sort the grades array in descending order

    maxGroups := 1 // At least one group can be formed
    totalSum := grades[0]
    totalCount := 1
    
    for i := 1; i < len(grades); i++ {
        totalSum += grades[i]
        totalCount++
        
        if totalSum >= grades[i]*(totalCount+1) {
            maxGroups++
        }
    }
    
    return maxGroups
}
