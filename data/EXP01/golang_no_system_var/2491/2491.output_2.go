Here is the solution for the given task:

```
func dividePlayers(skill []int) int64 {
    n := len(skill)
    
    totalSkill := 0
    for _, s := range skill {
        totalSkill += s
    }
    
    if totalSkill % (n/2) != 0 {
        return -1
    }
    
    targetSkill := totalSkill / (n/2)
    
    sort.Sort(sort.Reverse(sort.IntSlice(skill)))
    
    left := 0
    right := n - 1
    
    chemistry := int64(0)
    
    for left < right {
        if skill[left] + skill[right] == targetSkill {
            chemistry += int64(skill[left] * skill[right])
            left++
            right--
        } else if skill[left] + skill[right] < targetSkill {
            left++
        } else {
            right--
        }
    }
    
    return chemistry
}
```