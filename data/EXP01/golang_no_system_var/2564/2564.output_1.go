	"strconv"
	"strings"
)

func substringXorQueries(s string, queries [][]int) [][]int {
	n := len(s) // length of binary string s
	ans := make([][]int, len(queries))

	for i, q := range queries {
		first := strconv.Itoa(q[0])   // convert first integer to string
		second := strconv.Itoa(q[1])  // convert second integer to string
		left, right := -1, -1  // initialize left and right indices of substring
		
		for j := 0; j < n; j++ {
			for k := j; k < n; k++ {
				substr := s[j : k+1]  // extract substring from index j to k
				val, _ := strconv.ParseInt(substr, 2, 64)  // convert substring to decimal value
				
				if int(val) ^ q[0] == q[1] {
					if left == -1 || k-j < right-left {
						left = j
						right = k
					}
				}
			}
		}
		
		ans[i] = []int{left, right}
	}

	return ans
}