func repairCars(ranks []int, cars int) int64 {
    sort.Sort(sort.Reverse(sort.IntSlice(ranks)))

    totalTime := int64(0)

    carsRepaired := make([]int, len(ranks))

    for i := 0; i < cars; i++ {
        minTime := int64(1<<63 - 1)
        mechanicIdx := -1
        for j, rank := range ranks {
            time := (int64(rank) * int64(carsRepaired[j]+1) * int64(carsRepaired[j]+1))
            if time < minTime {
                minTime = time
                mechanicIdx = j
            }
        }

        carsRepaired[mechanicIdx]++
        totalTime = max(totalTime, minTime)
    }

    return totalTime
}

func max(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}