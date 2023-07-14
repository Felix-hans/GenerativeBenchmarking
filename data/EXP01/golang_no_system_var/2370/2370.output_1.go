func longestIdealString(s string, k int) int {
    n := len(s)
    dp := make([][]int, 26)
    for i := range dp {
        dp[i] = make([]int, k+1)
    }
    
    maxLen := 0
    for i := 0; i < n; i++ {
        for j := 0; j < 26; j++ {
            for l := 0; l <= k; l++ {
                if int(s[i]-'a') == j {
                    dp[j][l] = max(dp[j][l], l+1)
                } else {
                    dp[j][l] = max(dp[j][l], dp[int(s[i]-'a')][l]+1)
                }
            }
            maxLen = max(maxLen, dp[j][k])
        }
    }
    
    return maxLen
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
