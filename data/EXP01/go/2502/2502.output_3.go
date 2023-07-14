type Allocator struct {
    memory []int
}

func Constructor(n int) Allocator {
    return Allocator{
        memory: make([]int, n),
    }
}

func (this *Allocator) Allocate(size int, mID int) int {
    for i := 0; i <= len(this.memory)-size; i++ {
        available := true
        for j := i; j < i+size; j++ {
            if this.memory[j] != 0 {
                available = false
                break
            }
        }
        if available {
            for j := i; j < i+size; j++ {
                this.memory[j] = mID
            }
            return i
        }
    }
    return -1
}

func (this *Allocator) Free(mID int) int {
    count := 0
    for i := 0; i < len(this.memory); i++ {
        if this.memory[i] == mID {
            this.memory[i] = 0
            count++
        }
    }
    return count
}


