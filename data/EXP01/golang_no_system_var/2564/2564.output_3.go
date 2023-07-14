func substringXorQueries(s string, queries [][]int) [][]int {
	n := len(s)
	xorSum := make([]int, n+1)
	for i := 1; i <= n; i++ {
		xorSum[i] = xorSum[i-1] ^ int(s[i-1]-'0')
	}

	ans := make([][]int, len(queries))
	for i, query := range queries {
		left, right := query[0], query[1]
		xorValue := xorSum[right+1] ^ xorSum[left]

		leftIndex := -1
		for j := 0; j <= right; j++ {
			if xorSum[j] == xorValue {
				leftIndex = j
				break
			}
		}

		if leftIndex == -1 {
			ans[i] = []int{-1, -1}
		} else {
			rightIndex := leftIndex
			for j := right; j >= left; j-- {
				if xorSum[j] == xorValue {
					rightIndex = j
					break
				}
			}
			ans[i] = []int{leftIndex, rightIndex - 1} // Adjust the right endpoint by 1
		}
	}

	return ans
}
