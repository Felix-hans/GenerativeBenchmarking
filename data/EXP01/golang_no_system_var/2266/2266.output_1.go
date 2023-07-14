func countTexts(pressedKeys string) int {
	dp := make([]int, len(pressedKeys)+1)
	dp[0] = 1

	for i := 1; i <= len(pressedKeys); i++ {
		for j := 2; j <= 9; j++ {
			if pressedKeys[i-1] == byte(j+'0') {
				dp[i] = (dp[i] + dp[i-1]) % (1e9 + 7)
			}
		}
	}

	return dp[len(pressedKeys)]
}
