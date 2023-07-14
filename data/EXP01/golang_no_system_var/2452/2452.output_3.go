func twoEditWords(queries []string, dictionary []string) []string {
    result := []string{}
    
    for _, query := range queries {
        if containsWord(query, dictionary) || canTransform(query, dictionary) {
            result = append(result, query)
        }
    }
    
    return result
}

func containsWord(word string, dictionary []string) bool {
    for _, dictWord := range dictionary {
        if word == dictWord {
            return true
        }
    }
    return false
}

func canTransform(word string, dictionary []string) bool {
    for _, dictWord := range dictionary {
        if isOneEditAway(word, dictWord) || isTwoEditsAway(word, dictWord) {
            return true
        }
    }
    return false
}

func isOneEditAway(word1, word2 string) bool {
    diffCount := 0
    for i := range word1 {
        if word1[i] != word2[i] {
            diffCount++
            if diffCount > 1 {
                return false
            }
        }
    }
    return diffCount == 1
}

func isTwoEditsAway(word1, word2 string) bool {
    for i := range word1 {
        if word1[i] != word2[i] {
            editedWord := word1[:i] + word2[i:i+1] + word1[i+1:]
            if editedWord == word2 {
                return true
            }
            for j := range editedWord {
                if j != i && editedWord[j] != word2[j] {
                    editedWord = editedWord[:j] + word2[j:j+1] + editedWord[j+1:]
                    if editedWord == word2 {
                        return true
                    }
                }
            }
            return false
        }
    }
    return false
}
