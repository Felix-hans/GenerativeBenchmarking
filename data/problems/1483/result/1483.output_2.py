# @lc app=leetcode id=1483 lang=python3
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.max_level = 16  # Assuming the maximum height of the tree is 16 (can be adjusted based on constraints)
        self.ancestors = [[-1] * self.max_level for _ in range(n)]

        for i in range(n):
            self.ancestors[i][0] = parent[i]

        for level in range(1, self.max_level):
            for node in range(n):
                if self.ancestors[node][level - 1] != -1:
                    parent = self.ancestors[node][level - 1]
                    self.ancestors[node][level] = self.ancestors[parent][level - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        level = self.max_level - 1

        while node != -1 and k > 0:
            if k & 1:
                node = self.ancestors[node][level]
            level -= 1
            k >>= 1

        return node