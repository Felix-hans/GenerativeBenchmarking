func minimizeResult(expression string) string {
    var result string
    n := len(expression)
    for i := 0; i < n; i++ {
        if expression[i] == '+' {
            result = expression[:i-1] + "(" + expression[i-1:i+2] + ")" + expression[i+2:]
            break
        }
    }
    return result
}
