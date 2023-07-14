type Allocator struct {
    memory []int
    allocatedBlocks map[int][]int
}

func Constructor(n int) Allocator {
    memory := make([]int, n)
    allocatedBlocks := make(map[int][]int)
    
    return Allocator{
        memory: memory,
        allocatedBlocks: allocatedBlocks,
    }
}

func (this *Allocator) Allocate(size int, mID int) int {
    for i := 0; i <= len(this.memory)-size; i++ {
        if this.memory[i] == 0 {
            isFreeBlock := true
            for j := i; j < i+size; j++ {
                if this.memory[j] != 0 {
                    isFreeBlock = false
                    break
                }
            }
            if isFreeBlock {
                for j := i; j < i+size; j++ {
                    this.memory[j] = mID
                }
                this.allocatedBlocks[mID] = append(this.allocatedBlocks[mID], i)
                return i
            }
        }
    }
    return -1
}

func (this *Allocator) Free(mID int) int {
    count := 0
    if blocks, ok := this.allocatedBlocks[mID]; ok {
        for _, block := range blocks {
            for i := block; i < block+len(blocks); i++ {
                this.memory[i] = 0
            }
            count += len(blocks)
        }
        delete(this.allocatedBlocks, mID)
    }
    return count
}


