func minGroups(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
    
    groups := 1
    prevEnd := intervals[0][1]
    
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] > prevEnd {
            groups++
        }
        prevEnd = max(prevEnd, intervals[i][1])
    }
    
    return groups
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
