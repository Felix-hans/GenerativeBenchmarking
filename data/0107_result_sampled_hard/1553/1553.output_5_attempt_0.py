# @lc app=leetcode id=1553 lang=python3
class Solution:
    def minDays(self, n: int) -> int:
        memo = {}  # Memoization dictionary

        def eatOranges(count):
            if count <= 1:
                return count

            if count in memo:
                return memo[count]

            result = 1 + eatOranges(count - 1)

            if count % 2 == 0:
                result = min(result, 1 + eatOranges(count // 2))

            if count % 3 == 0:
                result = min(result, 1 + eatOranges(count // 3 * 2))

            memo[count] = result
            return result

        return eatOranges(n)