func minSteps(s string, t string) int {
    count := make(map[byte]int)

    for i := 0; i < len(s); i++ {
        count[s[i]]++
    }

    steps := 0

    for i := 0; i < len(t); i++ {
        if count[t[i]] > 0 {
            count[t[i]]--
        } else {
            steps++
        }
    }

    return steps
}
