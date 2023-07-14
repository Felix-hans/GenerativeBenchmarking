  "strings"
  "sort"
)

func longestIdealString(s string, k int) int {
  if len(s) == 0 {
    return 0
  }
  
  maxLenMap := make(map[string]int)
  
  letters := strings.Split(s, "")
  
  sort.Strings(letters)
  
  maxLen := 0
  
  for i := 0; i < len(letters); i++ {
    letter := letters[i]
    
    prevMaxLen := maxLenMap[letter]
    
    curMaxLen := 1
    
    for j := i - 1; j >= 0; j-- {
      prevLetter := letters[j]
      
      diff := int(letter[0]) - int(prevLetter[0])
      if diff < 0 {
        diff = -diff
      }
      
      if diff <= k {
        curMaxLen = max(curMaxLen, maxLenMap[prevLetter]+1)
      }
    }
    
    maxLen = max(maxLen, curMaxLen)
    
    maxLenMap[letter] = curMaxLen
  }
  
  return maxLen
}

func max(a, b int) int {
  if a > b {
    return a
  }
  return b
}