func minimumPartition(s string, k int) int {
    partition := 0
    substringValue := 0
    
    for _, char := range s {
        digit := int(char - '0')
        substringValue += digit
        
        if substringValue > k {
            return -1
        }
        
        if substringValue == k {
            partition++
            substringValue = 0
        }
    }
    
    if substringValue != 0 {
        partition++
    }
    
    return partition
}
