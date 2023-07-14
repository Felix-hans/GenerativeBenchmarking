func successfulPairs(spells []int, potions []int, success int64) []int {
    sort.Ints(potions)
    pairs := make([]int, len(spells))
    
    for i := 0; i < len(spells); i++ {
        spell := int64(spells[i])
        count := binarySearch(potions, success/spell) - 1
        if count < 0 {
            count = 0
        }
        pairs[i] = count
    }
    
    return pairs
}

func binarySearch(arr []int, target int64) int {
    left := 0
    right := len(arr)
    
    for left < right {
        mid := left + (right-left)/2
        if int64(arr[mid]) < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    
    return left
}
