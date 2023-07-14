func secondsToRemoveOccurrences(s string) int {
    count := 0
    for strings.Contains(s, "01") {
        s = strings.Replace(s, "01", "10", -1)
        count++
    }
    return count
}
