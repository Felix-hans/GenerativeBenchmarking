func maximumGroups(grades []int) int {
    sort.Ints(grades)
    numGroups := 0
    currSum := 0
    currCount := 0

    for i := 0; i < len(grades); i++ {
        currSum += grades[i]
        currCount++

        if i < len(grades)-1 && currSum >= grades[i+1] {
            numGroups++
            currSum = 0
            currCount = 0
        }
    }

    if currCount > 0 {
        numGroups++
    }

    return numGroups
}
