func countGoodStrings(low int, high int, zero int, one int) int {
    const mod = int(1e9 + 7)
    n := high - low + 1
    dp := make([][][]int, n+1)

    for i := range dp {
        dp[i] = make([][]int, zero+1)
        for j := range dp[i] {
            dp[i][j] = make([]int, one+1)
        }
    }

    dp[0][0][0] = 1

    for i := 1; i <= n; i++ {
        for z := 0; z <= zero; z++ {
            for o := 0; o <= one; o++ {
                dp[i][z][o] = (dp[i][z][o] + dp[i-1][z][o]) % mod

                if o > 0 && i <= high-low+1-z {
                    dp[i][z][o] = (dp[i][z][o] + dp[i-1][z][o-1]) % mod
                }
            }
        }
    }

    count := 0
    for z := 0; z <= zero; z++ {
        for o := 0; o <= one; o++ {
            if low <= z+o && z+o <= high {
                count = (count + dp[n][z][o]) % mod
            }
        }
    }

    return count
}

