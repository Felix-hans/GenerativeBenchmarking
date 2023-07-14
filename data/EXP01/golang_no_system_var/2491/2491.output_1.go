func dividePlayers(skill []int) int64 {
    sum := 0
    for _, s := range skill {
        sum += s
    }
    
    if sum%(len(skill)/2) != 0 {
        return -1
    }
    
    target := sum / (len(skill) / 2)
    
    counts := make(map[int]int)
    for _, s := range skill {
        counts[s]++
    }
    
    for s, count := range counts {
        if count%2 != 0 {
            return -1
        }
        
        numTeams := count / 2
        
        complement := target - s
        complementCount := counts[complement]
        numComplementTeams := complementCount / 2
        
        if numTeams > numComplementTeams {
            counts[complement] -= numComplementTeams * 2
            counts[s] -= numComplementTeams * 2
        } else {
            counts[complement] -= numTeams * 2
            counts[s] -= numTeams * 2
        }
    }
    
    chemistry := int64(0)
    for s, count := range counts {
        chemistry += int64(s) * int64(count/2)
    }
    
    return chemistry
}
