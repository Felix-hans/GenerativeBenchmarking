func twoSum(nums []int, target int) []int {
    numMap := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if _, ok := numMap[complement]; ok {
            return []int{numMap[complement], i}
        }
        numMap[num] = i
    }
    return []int{}
}