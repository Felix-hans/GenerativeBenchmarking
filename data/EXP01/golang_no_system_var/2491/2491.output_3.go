func dividePlayers(skill []int) int {
    totalSkills := 0
    for _, s := range skill {
        totalSkills += s
    }
    if totalSkills%2 != 0 {
        return -1
    }
    
    sort.Ints(skill)
    
    n := len(skill)
    sum := 0
    for i := 0; i < n/2; i++ {
        sum += skill[i] * skill[n-i-1]
    }
    
    return sum
}
