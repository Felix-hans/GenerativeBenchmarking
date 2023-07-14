func countGoodStrings(low int, high int, zero int, one int) int {
    mod := int(1e9) + 7
    dp := make([][]int, low+1)
    for i := 0; i <= low; i++ {
        dp[i] = make([]int, high+1)
    }

    dp[0][0] = 1

    for i := 0; i <= low; i++ {
        for j := 0; j <= high; j++ {
            if i > 0 && dp[i-1][j] >= low && dp[i-1][j] <= high {
                dp[i][j] = (dp[i][j] + dp[i-1][j]) % mod
            }
            if j > 0 && dp[i][j-1] >= low && dp[i][j-1] <= high {
                dp[i][j] = (dp[i][j] + dp[i][j-1]) % mod
            }
        }
    }

    result := 0
    for i := low; i <= high; i++ {
        result = (result + dp[zero][one]) % mod
    }

    return result
}
