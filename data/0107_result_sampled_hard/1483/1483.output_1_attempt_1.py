# @lc app=leetcode id=1483 lang=python3
from math import log2

class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.ancestors = [[-1] * (int(log2(n))+1) for _ in range(n)]
        
        for node in range(n):
            self.ancestors[node][0] = parent[node]
            
            for k in range(1, int(log2(n))+1):
                if self.ancestors[node][k-1] == -1:
                    break
                self.ancestors[node][k] = self.ancestors[self.ancestors[node][k-1]][k-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            i = int(log2(k))
            node = self.ancestors[node][i]
            k -= 2 ** i

        return node