func twoSum(nums []int, target int) []int {
    complement := make(map[int]int)
    
    for i, num := range nums {
        complementNum := target - num
        
        if j, ok := complement[complementNum]; ok {
            return []int{j, i}
        }
        
        complement[num] = i
    }
    
    return []int{}
}


    target := 9
    result := twoSum(nums, target)
    fmt.Println(result) // Output: [0 1]
}
