func longestContinuousSubstring(s string) int {
    maxLen := 0 // maximum substring length seen so far
    curLen := 1 // length of the current substring
    for i := 1; i < len(s); i++ {
        if s[i] >= s[i-1] {
            curLen++ // current substring is still alphabetical, increase length
        } else {
            maxLen = max(maxLen, curLen) // update maximum length if necessary
            curLen = 1 // reset current length
        }
    }
    return max(maxLen, curLen) // comparing the last substring with the maximum substring length
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
