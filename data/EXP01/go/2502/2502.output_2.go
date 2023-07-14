/*
* @lc app=leetcode id=2502 lang=golang
*
* [2502] Design Memory Allocator
*/

type Allocator struct {
    memory []int
    used   map[int]struct{}
}

func Constructor(n int) Allocator {
    return Allocator{
        memory: make([]int, n),
        used:   make(map[int]struct{}),
    }
}

func (this *Allocator) Allocate(size int, mID int) int {
    for i := 0; i <= len(this.memory)-size; i++ {
        found := true
        for j := i; j < i+size; j++ {
            if this.memory[j] != 0 {
                found = false
                break
            }
        }
        if found {
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
            count += 1
        }
    }
    delete(this.used, mID)
    return count
}

/**
 * Your Allocator object will be instantiated and called as such:
 * obj := Constructor(n);
 * param_1 := obj.Allocate(size,mID);
 * param_2 := obj.Free(mID);
 */
