const mod = int(1e9) + 7

func countTexts(pressedKeys string) int {
    mappings := map[byte]string{
        '2': "abc",
        '3': "def",
        '4': "ghi",
        '5': "jkl",
        '6': "mno",
        '7': "pqrs",
        '8': "tuv",
        '9': "wxyz",
    }

    combinations := make(map[string]bool)
    backtrack(pressedKeys, "", 0, mappings, combinations)

    return len(combinations) % mod
}

func backtrack(pressedKeys, combination string, index int, mappings map[byte]string, combinations map[string]bool) {
    if index == len(pressedKeys) {
        combinations[combination] = true
        return
    }

    digit := pressedKeys[index]
    letters := mappings[digit]

    for _, letter := range letters {
        combination += string(letter)
        backtrack(pressedKeys, combination, index+1, mappings, combinations)
        combination = combination[:len(combination)-1]
    }
}
