func minimumLines(stockPrices [][]int) int {
    if len(stockPrices) == 0 {
        return 0
    }
    
    count := 1 // start with one line
    prevPrice := stockPrices[0][1] // initialize the previous price to the first price in the array
    
    for i := 1; i < len(stockPrices); i++ {
        currPrice := stockPrices[i][1] // get the current price
        
        if currPrice != prevPrice {
            count++ // increment the count if the price changes
            prevPrice = currPrice // update the previous price to the current price
        }
    }
    
    return count
}
