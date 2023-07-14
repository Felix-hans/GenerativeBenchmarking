func dividePlayers(skill []int) int64 {
    n := len(skill)
    if n%2 != 0 {
        return -1
    }

    sort.Ints(skill)
    left, right := 0, n-1
    totalChemistry := int64(0)

    for left < right {
        chemistry := int64(skill[left] * skill[right])
        totalChemistry += chemistry
        left++
        right--
    }

    return totalChemistry
}
