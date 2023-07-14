func successfulPairs(spells []int, potions []int, success int64) []int {
    n := len(spells)
    m := len(potions)
    pairs := make([]int, n)

    for i := 0; i < n; i++ {
        spell := spells[i]
        for j := 0; j < m; j++ {
            potion := potions[j]
            if int64(spell)*int64(potion) >= success {
                pairs[i]++
            }
        }
    }

    return pairs
}
