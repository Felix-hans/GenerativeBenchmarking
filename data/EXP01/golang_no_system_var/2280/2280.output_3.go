func minimumLines(stockPrices [][]int) int {
    if len(stockPrices) <= 1 {
        return len(stockPrices)
    }
    
    lines := 1 // minimum number of lines needed to represent the line chart
    slope := float64(stockPrices[1][1] - stockPrices[0][1]) / float64(stockPrices[1][0] - stockPrices[0][0])

    for i := 2; i < len(stockPrices); i++ {
        newSlope := float64(stockPrices[i][1] - stockPrices[i-1][1]) / float64(stockPrices[i][0] - stockPrices[i-1][0])
        
        if newSlope != slope {
            slope = newSlope
            lines++
        }
    }
    
    return lines
}
