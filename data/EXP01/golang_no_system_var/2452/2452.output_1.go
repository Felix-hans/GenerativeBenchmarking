func twoEditWords(queries []string, dictionary []string) []string {
    result := []string{}
    
    for _, query := range queries {
        if contains(dictionary, query) {
            result = append(result, query)
        } else {
            for _, word := range dictionary {
                if isTransformable(query, word) {
                    result = append(result, query)
                    break
                }
            }
        }
    }
    
    return result
}

func contains(arr []string, word string) bool {
    for _, w := range arr {
        if w == word {
            return true
        }
    }
    return false
}

func isTransformable(query, word string) bool {
    diffCount := 0
    for i := 0; i < len(query); i++ {
        if query[i] != word[i] {
            diffCount++
            if diffCount > 2 {
                return false
            }
        }
    }
    return true
}
