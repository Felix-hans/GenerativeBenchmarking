func successfulPairs(spells []int, potions []int, success int64) []int {
    res := make([]int, len(spells))

    for i := 0; i < len(spells); i++ {
        for j := 0; j < len(potions); j++ {
            if int64(spells[i])*int64(potions[j]) >= success {
                res[i]++
            }
        }
    }

    return res
}


    potions := []int{1, 2, 3, 4, 5}
    success := int64(7)

    fmt.Println(successfulPairs(spells, potions, success)) // Output: [4, 0, 3]
}
