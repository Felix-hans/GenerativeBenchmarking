func countTexts(pressedKeys string) int {
    letters := []string{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"}
    mod := int(math.Pow10(9)) + 7

    var generateMessages func(idx int, currentMessage string, digitCount []int, letters []string, totalMessages int) int
    generateMessages = func(idx int, currentMessage string, digitCount []int, letters []string, totalMessages int) int {
        if idx == len(pressedKeys) {
            return (totalMessages + 1) % mod
        }

        digit := int(pressedKeys[idx] - '0')
        for _, letter := range letters[digit] {
            digitCount[digit]++
            totalMessages = generateMessages(idx+1, currentMessage+string(letter), digitCount, letters, totalMessages)
            digitCount[digit]--
        }

        return totalMessages
    }

    digitCount := make([]int, 10)
    totalMessages := generateMessages(0, "", digitCount, letters, 0)

    return totalMessages
}
