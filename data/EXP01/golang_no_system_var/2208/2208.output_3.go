func halveArray(nums []int) int {
   sort.Ints(nums)
   sum := 0
   for _, num := range nums {
      sum += num
   }
   target := sum / 2
   operations := 0
   for _, num := range nums {
      for num > target {
         num /= 2
         operations++
      }
      target -= num
   }
   return operations
}
