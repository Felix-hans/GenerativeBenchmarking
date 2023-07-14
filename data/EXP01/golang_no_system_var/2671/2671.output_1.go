type FrequencyTracker struct {
    numbers map[int]int
}

func Constructor() FrequencyTracker {
    return FrequencyTracker{
        numbers: make(map[int]int),
    }
}

func (ft *FrequencyTracker) Add(number int) {
    ft.numbers[number]++
}

func (ft *FrequencyTracker) DeleteOne(number int) {
    if _, ok := ft.numbers[number]; ok {
        ft.numbers[number]--
        if ft.numbers[number] == 0 {
            delete(ft.numbers, number)
        }
    }
}

func (ft *FrequencyTracker) HasFrequency(frequency int) bool {
    for _, count := range ft.numbers {
        if count == frequency {
            return true
        }
    }
    return false
}
