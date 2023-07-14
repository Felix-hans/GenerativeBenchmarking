func repairCars(ranks []int, cars int) int64 {
    sort.Sort(sort.Reverse(sort.IntSlice(ranks))) // Sort ranks in descending order
    var time int64

    for i, rank := range ranks {
        repairableCars := rank * (i+1) * (i+1) // Calculate number of cars this mechanic can repair

        if repairableCars >= cars {
            time += int64(cars) * int64((i+1) * (i+1))
            break // All cars have been repaired
        } else {
            time += int64(repairableCars) * int64((i+1) * (i+1))
            cars -= repairableCars // Update the number of remaining cars
        }
    }

    return time
}
