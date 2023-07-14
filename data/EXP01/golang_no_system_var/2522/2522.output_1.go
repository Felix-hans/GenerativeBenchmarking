func minimumPartition(s string, k int) int {
    maxDigit, count := 0, 0 // variables to track maximum digit and count of substrings
    for i := 0; i < len(s); i++ {
        digit := int(s[i] - '0') // convert character to integer
        if digit > maxDigit {
            maxDigit = digit // update the maximum digit
        }
        if maxDigit > k {
            return -1 // no good partition exists
        }
        if digit == k {
            count++ // increment count if the digit is equal to k
        }
    }
    return count // return the count of substrings
}
