type Allocator struct {
    memory []int
}

func Constructor(n int) Allocator {
    return Allocator{
        memory: make([]int, n),
    }
}

func (a *Allocator) Allocate(size int, mID int) int {
    for i := 0; i <= len(a.memory)-size; i++ {
        if a.isMemoryFree(i, size) {
            a.assignMemory(i, size, mID)
            return i
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

func (a *Allocator) isMemoryFree(startIndex, size int) bool {
    for i := startIndex; i < startIndex+size; i++ {
        if a.memory[i] != 0 {
            return false
        }
    }
    return true
}

func (a *Allocator) assignMemory(startIndex, size, mID int) {
    for i := startIndex; i < startIndex+size; i++ {
        a.memory[i] = mID
    }
}
