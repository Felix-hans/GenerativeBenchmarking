func countDistinctIntegers(nums []int) int {
    distinctIntegers := make(map[int]bool)

    for _, num := range nums {
        distinctIntegers[num] = true
        numStr := strconv.Itoa(num)
        reversed := reverse(numStr)
        reversedNum, _ := strconv.Atoi(reversed)
        distinctIntegers[reversedNum] = true
    }

    return len(distinctIntegers)
}

func reverse(str string) string {
    reversed := ""
    for i := len(str) - 1; i >= 0; i-- {
        reversed += string(str[i])
    }
    return reversed
}
