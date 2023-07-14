func wordCount(startWords []string, targetWords []string) int {
    freq := make(map[string]int)
    for _, word := range startWords {
        freq[word]++
    }
    
    count := 0
    for i := 0; i < len(targetWords); i++ {
        target := targetWords[i]
        found := false
        for j := 0; j < len(startWords); j++ {
            start := startWords[j]
            if len(target)-len(start) != 1 {
                continue
            }
            
            diff := make([]int, 26)
            for k := 0; k < len(start); k++ {
                diff[int(start[k]-'a')]++
            }
            for k := 0; k < len(target); k++ {
                diff[int(target[k]-'a')]--
            }
            
            nonZeroCount := 0
            for _, val := range diff {
                if val != 0 {
                    nonZeroCount++
                }
            }
            
            if nonZeroCount == 1 {
                found = true
                break
            }
        }
        if found {
            count++
        }
    }
    
    return count
}
