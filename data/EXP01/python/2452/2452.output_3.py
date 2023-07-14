# @lc app=leetcode id=2452 lang=python3
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def generate_edit_words(word, edits):
            words = set()
            for i in range(len(word)):
                for letter in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + letter + word[i+1:]
                    if edits == 2:
                        words.update(generate_edit_words(new_word, edits - 1))
                    else:
                        words.add(new_word)
            return words
        
        result = []
        for query in queries:
            edit_words_1 = generate_edit_words(query, 1)
            edit_words_2 = generate_edit_words(query, 2)
            
            if any(word in dictionary for word in edit_words_1) or any(word in dictionary for word in edit_words_2):
                result.append(query)
        
        return result