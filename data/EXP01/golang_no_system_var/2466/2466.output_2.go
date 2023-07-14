const mod = int(1e9) + 7

func countGoodStrings(low int, high int, zero int, one int) int {
    dp := make([][2]int, high+1)
    dp[0][0] = 1

    for i := 1; i <= high; i++ {
        dp[i][0] = (dp[i-1][0] + dp[i-1][1]) * zero % mod
        dp[i][1] = dp[i-1][0] * one % mod
    }

    count := 0
    for i := low; i <= high; i++ {
        count = (count + dp[i][0] + dp[i][1]) % mod
    }

    return count
}
