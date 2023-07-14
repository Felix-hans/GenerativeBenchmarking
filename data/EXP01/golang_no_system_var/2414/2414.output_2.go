func longestContinuousSubstring(s string) int {
    maxLen := 0
    currLen := 1

    for i := 1; i < len(s); i++ {
        if s[i] > s[i-1] {
            currLen++
        } else {
            currLen = 1
        }
        if currLen > maxLen {
            maxLen = currLen
        }
    }

    return maxLen
}
