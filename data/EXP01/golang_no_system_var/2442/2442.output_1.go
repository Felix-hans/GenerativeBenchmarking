func countDistinctIntegers(nums []int) int {
    distinctIntegers := make(map[int]bool)
    
    for _, num := range nums {
        distinctIntegers[num] = true
        
        reverseNum := reverseDigits(num)
        distinctIntegers[reverseNum] = true
    }
    
    return len(distinctIntegers)
}

func reverseDigits(num int) int {
    reversed := 0
    
    for num > 0 {
        digit := num % 10
        reversed = reversed*10 + digit
        num /= 10
    }
    
    return reversed
}