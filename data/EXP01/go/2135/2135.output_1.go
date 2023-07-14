func wordCount(startWords []string, targetWords []string) int {
    count := 0
    for _, target := range targetWords {
        for _, start := range startWords {
            if isConvertible(start, target) {
                count++
                break
            }
        }
    }
    return count
}

func isConvertible(start, target string) bool {
    charCount := make(map[rune]int)
    for _, ch := range target {
        charCount[ch]++
    }
    for _, ch := range start {
        charCount[ch]--
    }
    for _, count := range charCount {
        if count > 0 {
            return false
        }
    }
    return true
}
