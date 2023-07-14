func dividePlayers(skill []int) int64 {
    sum := int64(0)
    for _, s := range skill {
        sum += int64(s)
    }
    if sum%2 != 0 {
        return -1
    }
    target := sum / 2
    return getChemistry(skill, 0, target)
}

func getChemistry(skill []int, idx int, target int64) int64 {
    if target == 0 {
        return 1
    }
    if target < 0 || idx >= len(skill) {
        return -1
    }
    count1 := getChemistry(skill, idx+1, target-int64(skill[idx]))
    count2 := getChemistry(skill, idx+1, target)
    if count1 == -1 && count2 == -1 {
        return -1
    } else if count1 == -1 {
        return count2
    } else if count2 == -1 {
        return count1
    } else {
        return 1 + max(count1, count2)
    }
}

func max(a, b int64) int64 {
    if a > b {
        return a
    }
    return b
}


    result := dividePlayers(skill)
    fmt.Println(result) // Output: 22
}
