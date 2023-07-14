	"strconv"
)

func minimizeResult(expression string) string {
	n := len(expression)
	pivot := 0

	for i := 0; i < n; i++ {
		if expression[i] == '+' {
			pivot = i
			break
		}
	}

	num1, _ := strconv.Atoi(expression[:pivot])
	num2, _ := strconv.Atoi(expression[pivot+1:])

	result1 := num1 + num2
	result2 := num1*(num2)
	result3 := (num1) + num2

	if result1 <= result2 && result1 <= result3 {
		return expression
	} else if result2 <= result3 {
		return strconv.Itoa(num1) + "+" + strconv.Itoa(num2)
	} else {
		return strconv.Itoa(num1) + "+" + strconv.Itoa(num2)
	}
}
