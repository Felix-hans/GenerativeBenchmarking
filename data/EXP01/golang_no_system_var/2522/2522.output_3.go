func minimumPartition(s string, k int) int {
    count := 0
    value := 0
    for i := 0; i < len(s); i++ {
        digit := int(s[i] - '0') // convert character to integer
        value = value*10 + digit // update the value of the current substring
        
        if value > k {
            return -1
        }
        
        if value != 0 && (i == len(s)-1 || value*10+int(s[i+1]-'0') > k) {
            count++ // increment the count of substrings
            value = 0 // reset the value of the current substring
        }
    }
    return count
}
