func minimizeResult(expression string) string {
    num1 := ""
    num2 := ""

    i := 0

    for expression[i] != '+' {
        num1 += string(expression[i])
        i++
    }
    i++
    for i < len(expression) {
        num2 += string(expression[i])
        i++
    }

    sum := strconv.Itoa(strconv.Atoi(num1) + strconv.Atoi(num2))

    result := ""

    if sum == "0" {
        result = "(" + num1 + "+" + num2 + ")"
    } else if len(num1) <= len(num2) {
        result = "(" + num1 + "+" + num2 + ")"
    } else {
        result = "(" + num1 + "+" + num2
        result += ")"
    }

    return result
}
