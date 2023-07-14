func minSteps(s string, t string) int {
    sCount := make([]int, 26)
    tCount := make([]int, 26)
    
    for i := 0; i < len(s); i++ {
        sCount[s[i]-'a']++
    }
    
    for i := 0; i < len(t); i++ {
        tCount[t[i]-'a']++
    }
    
    steps := 0
    for i := 0; i < 26; i++ {
        if sCount[i] > tCount[i] {
            steps += sCount[i] - tCount[i]
        }
    }
    
    return steps
}
