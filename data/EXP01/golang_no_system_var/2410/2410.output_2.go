func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Ints(players)
    sort.Ints(trainers)

    count := 0

    for _, player := range players {
        found := false
        for i, trainer := range trainers {
            if player <= trainer {
                found = true
                count++
                trainers = append(trainers[:i], trainers[i+1:]...)
                break
            }
        }
        if !found {
            break
        }
    }

    return count
}
