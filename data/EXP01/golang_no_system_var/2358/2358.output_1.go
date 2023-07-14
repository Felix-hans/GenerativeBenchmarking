func maximumGroups(grades []int) int {
    sort.Ints(grades)
    
    sum := grades[0]
    count := 1
    groupCount := 1
    
    for i := 1; i < len(grades); i++ {
        if sum > grades[i] || count > i {
            groupCount++
            sum = grades[i]
            count = 1
        } else {
            sum += grades[i]
            count++
        }
    }
    
    return groupCount
}
