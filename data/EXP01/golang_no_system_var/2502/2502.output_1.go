type Allocator struct {
    memory []int
    allocations map[int][]int
}

func Constructor(n int) Allocator {
    memory := make([]int, n)
    return Allocator{
        memory: memory,
        allocations: make(map[int][]int),
    }
}

func (a *Allocator) Allocate(size int, mID int) int {
    start := 0
    count := 0

    for i := 0; i < len(a.memory); i++ {
        if a.memory[i] == 0 {
            count++
        } else {
			count = 0
        }

        if count == size {
            for j := i - size + 1; j <= i; j++ {
                a.memory[j] = mID
            }

            if _, ok := a.allocations[mID]; !ok {
                a.allocations[mID] = []int{}
            }
            a.allocations[mID] = append(a.allocations[mID], i-size+1)

            return i - size + 1
        }
    }

    return -1
}

func (a *Allocator) Free(mID int) int {
    unitsFreed := 0

    if allocations, ok := a.allocations[mID]; ok {
        for _, start := range allocations {
            for i := start; i < len(a.memory) && a.memory[i] == mID; i++ {
                a.memory[i] = 0
                unitsFreed++
            }
        }

        delete(a.allocations, mID)
    }

    return unitsFreed
}
