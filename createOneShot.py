def getSolution(language):

    solutionDict = {
        'python':
        '''
        Here is the code implementation for the given task:

        ```python
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:
                complement_dict = {}
                for i, num in enumerate(nums):
                    complement = target - num
                    if complement in complement_dict:
                        return [complement_dict[complement], i]
                    complement_dict[num] = i
        ```

        Example usage:
        ```python
        if __name__ == "__main__":
            solution = Solution()
            nums = [2, 7, 11, 15]
            target = 9
            print(solution.twoSum(nums, target))
        ```

        ''',

        'csharp':
        '''
        Here is the code implementation for the given task:

        ```csharp
        public class Solution {
            public int[] TwoSum(int[] nums, int target) {
                Dictionary<int, int> map = new Dictionary<int, int>();
                for (int i = 0; i < nums.Length; i++) {
                    int complement = target - nums[i];
                    if (map.ContainsKey(complement)) {
                        return new int[]{map[complement], i};
                    }
                    map[nums[i]] = i;
                }
                throw new ArgumentException("No two sum solution");
            }
        }
        ```

        Example usage:
        ```csharp
        public class Main {
            public static void main(String[] args) {
                Solution solution = new Solution();
                int[] nums = {2, 7, 11, 15};
                int target = 9;
                int[] result = solution.twoSum(nums, target);
                System.out.println(result[0] + " " + result[1]);  // Expected output: 0 1
            }
        }
        ```
        ''',

        'java':
        '''
        Here is the code implementation for the given task:

        ```java

        class Solution {
            public int[] twoSum(int[] nums, int target) {
                int[] result = new int[2];
                Map<Integer, Integer> map = new HashMap<>();
                
                for (int i = 0; i < nums.length; i++) {
                    int complement = target - nums[i];
                    if (map.containsKey(complement)) {
                        result[0] = map.get(complement);
                        result[1] = i;
                        break;
                    }
                    map.put(nums[i], i);
                }
                
                return result;
            }
        }
        ```

        Example usage:
        ```java
        public class Main {
            public static void main(String[] args) {
                Solution solution = new Solution();
                int[] nums = {2, 7, 11, 15};
                int target = 9;
                int[] result = solution.twoSum(nums, target);
                System.out.println(result[0] + " " + result[1]);  // Expected output: 0 1
            }
        }
        ```
        ''',

        'javascript':
        '''
        Here is the code implementation for the given task:

        ```javascript
        var twoSum = function(nums, target) {
            const map = new Map();
            
            for (let i = 0; i < nums.length; i++) {
                const complement = target - nums[i];
                
                if (map.has(complement)) {
                    return [map.get(complement), i];
                }
                
                map.set(nums[i], i);
            }
            
            return [];
        };
        ```

        Example usage:
        ```javascript
        let nums = [2, 7, 11, 15];
        let target = 9;
        console.log(twoSum(nums, target)); 
        ```
        ''',

        'go':
        '''
        Here is the code implementation for the given task:

        ```go
        import "fmt"

        func twoSum(nums []int, target int) []int {
            numMap := make(map[int]int)
            for i, num := range nums {
                complement := target - num
                if _, ok := numMap[complement]; ok {
                    return []int{numMap[complement], i}
                }
                numMap[num] = i
            }
            return []int{}
        }
        ```


        Example usage:
        ```go
        func main() {
            nums := []int{2, 7, 11, 15}
            target := 9
            result := twoSum(nums, target)
            fmt.Println(result) // Output: [0 1]
        }
        ```
        ''',
        
        'ruby':
        '''
        Here is the code implementation for the given task:

        ```ruby
        def two_sum(nums, target)
            map = {}
            nums.each_with_index do |num, index|
                complement = target - num
                if map.include?(complement)
                    return [map[complement], index]
                end
                map[num] = index
            end
        end
        ```

        Example usage:
        ```ruby
        nums = [2, 7, 11, 15]
        target = 9
        puts two_sum(nums, target)  # Expected output: [0, 1]
        ```
        ''',
    }


    return solutionDict[language]

def chooseTemplate(language):

    templateDict = {
        'python':
        '''
        ```python
        class Solution:
            def twoSum(self, nums: List[int], target: int) -> List[int]:

        ```
        ''',

        'csharp':
        '''
        ```csharp
        /*
        * @lc app=leetcode id=1 lang=csharp
        *
        * [1] Two Sum
        */

        // @lc code=start
        public class Solution {
            public int[] TwoSum(int[] nums, int target) {
                
            }
        }
        // @lc code=end

        ```
        ''',

        'java':
        '''
        ```java
        /*
        * @lc app=leetcode id=1 lang=java
        *
        * [1] Two Sum
        */

        // @lc code=start
        class Solution {
            public int[] twoSum(int[] nums, int target) {
                
            }
        }
        // @lc code=end


        ```
        ''',

        'javascript':
        '''
        ```javascript
        /*
        * @lc app=leetcode id=1 lang=javascript
        *
        * [1] Two Sum
        */

        // @lc code=start
        /**
        * @param {number[]} nums
        * @param {number} target
        * @return {number[]}
        */
        var twoSum = function(nums, target) {
            
        };
        // @lc code=end

        ```
        ''',

        'go':
        '''
        ```go
        /*
        * @lc app=leetcode id=1 lang=golang
        *
        * [1] Two Sum
        */

        // @lc code=start
        func twoSum(nums []int, target int) []int {
            
        }
        // @lc code=end


        ```
        ''',

        'ruby':
        '''
        ```ruby
        #
        # @lc app=leetcode id=1 lang=ruby
        #
        # [1] Two Sum
        #

        # @lc code=start
        # @param {Integer[]} nums
        # @param {Integer} target
        # @return {Integer[]}
        def two_sum(nums, target)
            
        end
        # @lc code=end

        ```
        ''',
    }

    return templateDict[language]

def createOneShot(language):
    problem = '''
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Example 1:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


    Example 2:

    Input: nums = [3,2,4], target = 6
    Output: [1,2]


    Constraints:

    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    -10^9 <= target <= 10^9
    Only one valid answer exists.

    Follow-up: Can you come up with an algorithm that is less than O(n^2) time
    complexity?

    '''

    template = chooseTemplate(language)

    description = problem + template

    solution = getSolution(language)

    return description, solution