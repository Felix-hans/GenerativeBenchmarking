func minimumLines(stockPrices [][]int) int {
    n := len(stockPrices)
    if n == 0 {
        return 0
    }
    
    lines := 1
    prevSlope := float64(stockPrices[1][1] - stockPrices[0][1]) / float64(stockPrices[1][0] - stockPrices[0][0])
    
    for i := 2; i < n; i++ {
        slope := float64(stockPrices[i][1] - stockPrices[i-1][1]) / float64(stockPrices[i][0] - stockPrices[i-1][0])
        
        if slope != prevSlope {
            lines++
            prevSlope = slope
        }
    }
    
    return lines
}
