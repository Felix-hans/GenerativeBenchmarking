func twoSum(nums []int, target int) []int {
    complements := make(map[int]int)

    for i, num := range nums {
        if complementIndex, ok := complements[num]; ok {
            return []int{complementIndex, i}
        }

        complements[target-num] = i
    }

    return []int{}
}


    target := 9
    result := twoSum(nums, target)
    fmt.Println(result) // Output: [0, 1]
}
