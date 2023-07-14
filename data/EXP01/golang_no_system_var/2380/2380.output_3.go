func secondsToRemoveOccurrences(s string) int {
    seconds := 0

    for strings.Contains(s, "01") {
        s = strings.ReplaceAll(s, "01", "10")
        seconds++
    }

    return seconds
}
