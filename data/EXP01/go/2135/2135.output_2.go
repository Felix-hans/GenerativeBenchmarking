func wordCount(startWords []string, targetWords []string) int {
    count := 0
    wordMap := make(map[string]bool)
    for _, word := range startWords {
        wordMap[word] = true
    }
    for _, target := range targetWords {
        if checkWord(wordMap, target) {
            count++
        }
    }
    return count
}

func checkWord(wordMap map[string]bool, target string) bool {
    if _, ok := wordMap[target]; ok {
        return true
    }
    for c := 'a'; c <= 'z'; c++ {
        newWord := target + string(c)
        if _, ok := wordMap[newWord]; ok {
            return true
        }
    }
    return false
}
