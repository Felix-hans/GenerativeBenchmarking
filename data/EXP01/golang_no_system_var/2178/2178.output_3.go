func maximumEvenSplit(finalSum int64) []int64 {
    result := []int64{}

    evenNumber := finalSum / 2 * 2
    result = append(result, evenNumber)

    for finalSum > 0 && finalSum%2 == 0 {
        finalSum -= evenNumber
        evenNumber = finalSum / 2 * 2
        result = append(result, evenNumber)
    }

    if finalSum == 0 {
        return result
    }

    return []int64{}
}
