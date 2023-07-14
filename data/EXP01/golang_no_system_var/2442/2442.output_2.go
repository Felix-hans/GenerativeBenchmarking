func countDistinctIntegers(nums []int) int {
    distinctSet := make(map[int]bool)

    for _, num := range nums {
        distinctSet[num] = true
        reverseNum := reverseDigits(num)
        distinctSet[reverseNum] = true
    }

    return len(distinctSet)
}

func reverseDigits(num int) int {
    reverse := 0

    for num > 0 {
        remainder := num % 10
        reverse = reverse*10 + remainder
        num /= 10
    }

    return reverse
}
