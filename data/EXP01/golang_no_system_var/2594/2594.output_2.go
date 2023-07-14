func repairCars(ranks []int, cars int) int {
    sort.Sort(sort.Reverse(sort.IntSlice(ranks)))

    totalTime := 0
    totalCarsRepaired := 0

    for _, rank := range ranks {
        carsRepaired := min(cars, rank)
        time := rank * carsRepaired * carsRepaired
        totalTime += time
        totalCarsRepaired += carsRepaired
        cars -= carsRepaired

        if cars == 0 {
            break
        }
    }

    return totalTime
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
