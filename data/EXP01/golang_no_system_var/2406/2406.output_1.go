func minGroups(intervals [][]int) int {
    if len(intervals) == 0 {
        return 0
    }
  
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })
  
    groups := 1
    maxEnd := intervals[0][1]
  
    for i := 1; i < len(intervals); i++ {
        if intervals[i][0] > maxEnd {
            groups++
            maxEnd = intervals[i][1]
        } else {
            maxEnd = max(maxEnd, intervals[i][1])
        }
    }
  
    return groups
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
