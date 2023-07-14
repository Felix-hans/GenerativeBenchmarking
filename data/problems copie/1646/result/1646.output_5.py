# @lc app=leetcode id=1646 lang=python3
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1
        maximum = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            maximum = max(maximum, nums[i])

        return maximum