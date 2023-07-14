func minGroups(intervals [][]int) int {
    sort.Slice(intervals, func(i, j int) bool {
        return intervals[i][0] < intervals[j][0]
    })

    groups := 1
    endTime := intervals[0][1]

    for i := 1; i < len(intervals); i++ {
        if endTime < intervals[i][0] {
            groups++
            endTime = intervals[i][1]
        } else {
            if endTime < intervals[i][1] {
                endTime = intervals[i][1]
            }
        }
    }

    return groups
}
