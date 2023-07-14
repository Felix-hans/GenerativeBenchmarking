func twoSum(nums []int, target int) []int {
    compMap := make(map[int]int)
    
    for i, num := range nums {
        
        if j, ok := compMap[num]; ok {
            return []int{j, i}
        }
        
        compMap[target-num] = i
    }
    
    return []int{}
}
