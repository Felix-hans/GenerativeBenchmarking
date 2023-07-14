# @lc app=leetcode id=212 lang=python3
class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['_end'] = True

        def dfs(i, j, node, path):
            char = board[i][j]
            if char in node:
                path += char
                node = node[char]
                if '_end' in node:
                    result.append(path)
                    del node['_end']  # Remove the word from trie to avoid duplicates

                board[i][j] = '#'

                if i > 0: dfs(i - 1, j, node, path)
                if i < len(board) - 1: dfs(i + 1, j, node, path)
                if j > 0: dfs(i, j - 1, node, path)
                if j < len(board[0]) - 1: dfs(i, j + 1, node, path)

                board[i][j] = char

        result = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie, "")

        return result