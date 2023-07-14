func minSteps(s string, t string) int {
    countS := make(map[byte]int)
    for i := 0; i < len(s); i++ {
        countS[s[i]]++
    }
    
    countT := make(map[byte]int)
    for i := 0; i < len(t); i++ {
        countT[t[i]]++
    }
    
    diff := 0
    for char, count := range countS {
        if countT[char] < count {
            diff += count - countT[char]
        }
    }
    
    return diff
}
