type Allocator struct {
    memory []int
}

func Constructor(n int) Allocator {
    memory := make([]int, n)
    return Allocator{memory: memory}
}

func (a *Allocator) Allocate(size int, mID int) int {
    for i := 0; i <= len(a.memory)-size; i++ {
        if a.memory[i] == 0 {
            isBlockAvailable := true
            for j := i; j < i+size; j++ {
                if a.memory[j] != 0 {
                    isBlockAvailable = false
                    break
                }
            }
            if isBlockAvailable {
                for j := i; j < i+size; j++ {
                    a.memory[j] = mID
                }
                return i
            }
        }
    }
    return -1
}

func (a *Allocator) Free(mID int) int {
    count := 0
    for i := 0; i < len(a.memory); i++ {
        if a.memory[i] == mID {
            a.memory[i] = 0
            count++
        }
    }
    return count
}
