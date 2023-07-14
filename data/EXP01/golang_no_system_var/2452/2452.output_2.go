func twoEditWords(queries []string, dictionary []string) []string {
    matches := []string{}
    
    for _, query := range queries {
        if checkMatch(query, dictionary) {
            matches = append(matches, query)
        }
    }
    
    return matches
}

func checkMatch(query string, dictionary []string) bool {
    for _, word := range dictionary {
        if query == word {
            return true
        }
        
        if isOneEditAway(query, word) {
            return true
        }
        
        if isTwoEditsAway(query, word) {
            return true
        }
    }
    
    return false
}

func isOneEditAway(word1 string, word2 string) bool {
    count := 0
    
    for i := 0; i < len(word1); i++ {
        if word1[i] != word2[i] {
            count++
        }
        
        if count > 1 {
            return false
        }
    }
    
    return count == 1
}

func isTwoEditsAway(word1 string, word2 string) bool {
    edits := 0
    i := 0
    j := 0
    
    for i < len(word1) && j < len(word2) {
        if word1[i] != word2[j] {
            edits++
            if edits > 2 {
                return false
            }
        } else {
            i++
        }
        
        j++
    }
    
    return edits == 2
}
