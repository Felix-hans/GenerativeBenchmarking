func wordCount(startWords []string, targetWords []string) int {
    startFreq := make(map[string]int)
    for _, word := range startWords {
        startFreq[word]++
    }

    count := 0
    for _, target := range targetWords {
        for i := 'a'; i <= 'z'; i++ {
            newWord := target + string(i)
            if startFreq[newWord] > 0 {
                count++
                break
            }
        }
    }

    return count
}
