func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Ints(players)
    sort.Ints(trainers)

    playerIdx, trainerIdx := 0, 0
    matches := 0

    for playerIdx < len(players) && trainerIdx < len(trainers) {
        if players[playerIdx] <= trainers[trainerIdx] {
            playerIdx++
            trainerIdx++
            matches++
        } else {
            trainerIdx++
        }
    }

    return matches
}
