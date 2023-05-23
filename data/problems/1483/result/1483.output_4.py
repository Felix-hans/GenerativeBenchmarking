# @lc app=leetcode id=1483 lang=python3
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        max_height = int(math.log2(n)) + 1

        self.ancestors = [[-1] * max_height for _ in range(n)]

        for node in range(n):
            self.ancestors[node][0] = parent[node]

        for k in range(1, max_height):
            for node in range(n):
                if self.ancestors[node][k-1] != -1:
                    self.ancestors[node][k] = self.ancestors[self.ancestors[node][k-1]][k-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            highest_bit = int(math.log2(k))
            
            node = self.ancestors[node][highest_bit]
            
            k -= 1 << highest_bit

        return node