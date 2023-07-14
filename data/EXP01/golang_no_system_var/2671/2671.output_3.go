type FrequencyTracker struct {
    data map[int]int
}

func Constructor() FrequencyTracker {
    return FrequencyTracker{
        data: make(map[int]int),
    }
}

func (this *FrequencyTracker) Add(number int) {
    this.data[number]++
}

func (this *FrequencyTracker) DeleteOne(number int) {
    if this.data[number] > 0 {
        this.data[number]--
    }
}

func (this *FrequencyTracker) HasFrequency(frequency int) bool {
    for _, count := range this.data {
        if count == frequency {
            return true
        }
    }
    return false
}
