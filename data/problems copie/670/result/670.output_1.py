# @lc app=leetcode id=670 lang=python3
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_str = str(num)
        n = len(num_str)

        last_occurrence = [0] * 10
        for i in range(n):
            last_occurrence[int(num_str[i])] = i

        for i in range(n):
            digit = int(num_str[i])

            for j in range(9, digit, -1):
                if last_occurrence[j] > i:
                    num_list = list(num_str)
                    num_list[i], num_list[last_occurrence[j]] = num_list[last_occurrence[j]], num_list[i]
                    return int(''.join(num_list))

        return num