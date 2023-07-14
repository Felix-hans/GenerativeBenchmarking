func maximumEvenSplit(finalSum int64) []int64 {
    var result []int64
    divisor := int64(2)

    for finalSum > 0 && divisor <= finalSum {
        if finalSum-divisor != divisor && (finalSum-divisor)%2 == 0 {
            result = append(result, divisor)
            finalSum -= divisor
        }
        divisor += 2
    }

    if finalSum == 0 {
        return result
    }
  
    return []int64{}
}
