func substringXorQueries(s string, queries [][]int) [][]int {
    n := len(s)
    ans := make([][]int, len(queries))
    
    prefixXor := make([]int, n+1)
    for i := 1; i <= n; i++ {
        prefixXor[i] = prefixXor[i-1] ^ int(s[i-1]-'0')
    }
    
    for i, query := range queries {
        left := query[0]
        right := query[1]
        
        for j := left; j <= right; j++ {
            for k := j+1; k <= right; k++ {
                xor := prefixXor[k] ^ prefixXor[j]
                if xor == query[0] {
                    ans[i] = []int{j, k-1}
                    break
                }
            }
            
            if ans[i] != nil {
                break
            }
        }
        
        if ans[i] == nil {
            ans[i] = []int{-1, -1}
        }
    }
    
    return ans
}
