# @lc app=leetcode id=2452 lang=python3
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_edit_distance_one(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            count_diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count_diff += 1
                    if count_diff > 1:
                        return False
            return count_diff == 1
        
        def is_edit_distance_two(s: str, t: str) -> bool:
            if len(s) != len(t):
                return False
            count_diff = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count_diff += 1
                    if count_diff > 2:
                        return False
            return count_diff == 2
        
        result = []
        for query in queries:
            for word in dictionary:
                if query == word or is_edit_distance_one(query, word) or is_edit_distance_two(query, word):
                    result.append(query)
                    break
        return result