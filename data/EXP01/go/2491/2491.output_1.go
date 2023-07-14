func dividePlayers(skill []int) int64 {
    totalSkill := 0
    skillCount := make(map[int]int)
    for _, s := range skill {
        totalSkill += s
        skillCount[s]++
    }
    
    if totalSkill%2 != 0 {
        return -1
    }
    
    target := totalSkill / 2
    dp := make([]int64, target+1)
    dp[0] = 1
    
    for s, count := range skillCount {
        for j := target; j >= s; j-- {
            for k := 1; k <= count; k++ {
                if j >= k*s {
                    dp[j] += dp[j-k*s]
                }
            }
        }
    }
    
    return dp[target]
}


    result := dividePlayers(skill)
    fmt.Println(result) // Output: 22
}
