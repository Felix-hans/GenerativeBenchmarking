func matchPlayersAndTrainers(players []int, trainers []int) int {
    sort.Ints(players)
    sort.Ints(trainers)

    playerPtr := 0
    trainerPtr := 0
    count := 0

    for playerPtr < len(players) && trainerPtr < len(trainers) {
        if players[playerPtr] <= trainers[trainerPtr] {
            count++
            playerPtr++
            trainerPtr++
        } else {
            trainerPtr++
        }
    }

    return count
}
