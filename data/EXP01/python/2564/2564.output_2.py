# @lc app=leetcode id=2564 lang=python3
from typing import List

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        xorArr = [0]
        for i in range(len(s)):
            xorArr.append(xorArr[-1] ^ int(s[i]))

        xorMap = {}
        for i in range(len(xorArr)):
            if xorArr[i] not in xorMap:
                xorMap[xorArr[i]] = i

        result = []
        for query in queries:
            first, second = query
            if second not in xorMap:
                result.append([-1, -1])
            else:
                start = xorMap[second]
                end = -1

                for i in range(start, len(xorArr)):
                    if xorArr[i] ^ xorArr[start - 1] == first:
                        end = i
                        break
                
                result.append([start - 1, end - 1])

        return result