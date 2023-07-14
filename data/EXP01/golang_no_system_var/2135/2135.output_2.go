func wordCount(startWords []string, targetWords []string) int {
    count := 0
    for _, target := range targetWords {
        for _, start := range startWords {
            if len(start)-len(target) == 0 {
                startRunes := []rune(start)
                targetRunes := []rune(target)
                sort.Slice(startRunes, func(i, j int) bool { return startRunes[i] < startRunes[j] })
                sort.Slice(targetRunes, func(i, j int) bool { return targetRunes[i] < targetRunes[j] })
                if string(startRunes) == string(targetRunes) {
                    count++
                    break
                }
            } else if len(start)-len(target) == 1 {
                startRunes := []rune(start)
                targetRunes := []rune(target)
                foundLetters := make(map[rune]bool)
                for _, letter := range startRunes {
                    foundLetters[letter] = true
                }
                possible := true
                for _, letter := range targetRunes {
                    if !foundLetters[letter] {
                        possible = false
                        break
                    }
                }
                if possible {
                    count++
                    break
                }
            }
        }
    }
    return count
}
