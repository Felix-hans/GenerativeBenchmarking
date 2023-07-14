func validPartition(nums []int) bool {
    n := len(nums)
    if n < 3 {
        return false
    }

    isValid := func(arr []int) bool {
        m := len(arr)
        if m == 2 && arr[0] == arr[1] {
            return true
        } else if m == 3 && (arr[0] == arr[1] && arr[1] == arr[2] || arr[0]+1 == arr[1] && arr[1]+1 == arr[2]) {
            return true
        }
        return false
    }

    start := 0
    for start < n-1 {
        end := start + 2
        curr := []int{}
        for end < n && !isValid(curr) {
            curr = nums[start : end+1]
            end++
        }
        if isValid(curr) {
            return true
        }
        start++
    }

    return false
}
