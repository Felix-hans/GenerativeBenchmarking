func longestIdealString(s string, k int) int {
    n := len(s)
    dp := make([][]int, n+1)
    for i := 0; i <= n; i++ {
        dp[i] = make([]int, 26)
    }

    for i := 0; i < 26; i++ {
        dp[0][i] = -1
    }

    for i := 1; i <= n; i++ {
        currentChar := int(s[i-1] - 'a')

        for j := 0; j < 26; j++ {
            nextChar := (j + k) % 26
            dp[i][currentChar] = max(dp[i][currentChar], dp[i-1][j]+1)
            dp[i][currentChar] = max(dp[i][currentChar], dp[i-1][nextChar]+1)
        }

        for j := 0; j < 26; j++ {
            dp[i][j] = max(dp[i][j], dp[i-1][j])
        }
    }

    longest := 0
    for i := 0; i < 26; i++ {
        longest = max(longest, dp[n][i])
    }

    return longest
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
