func triangularSum(nums []int) int {
    n := len(nums)

    for n > 1 {
        newNums := make([]int, n-1)
        for i := 0; i < n-1; i++ {
            newNums[i] = (nums[i] + nums[i+1]) % 10
        }
        nums = newNums
        n = len(nums)
    }

    return nums[0]
}
