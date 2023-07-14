# @lc app=leetcode id=2452 lang=python3
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_valid_edit(word1: str, word2: str) -> bool:
            if word1 == word2:
                return True
            elif len(word1) != len(word2):
                return False
            else:
                diff_count = 0
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        diff_count += 1
                    if diff_count > 2:
                        return False
                return True
        
        valid_words = []
        for query in queries:
            for d in dictionary:
                if is_valid_edit(query, d):
                    valid_words.append(query)
                    break
        return valid_words