# @lc app=leetcode id=1483 lang=python3
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.MAX_LOG = 20  # Maximum log value (assuming n <= 10^5)
        self.n = n
        self.ancestors = [[-1] * self.MAX_LOG for _ in range(n)]

        for node in range(n):
            self.ancestors[node][0] = parent[node]

        for log in range(1, self.MAX_LOG):
            for node in range(n):
                if self.ancestors[node][log - 1] != -1:
                    self.ancestors[node][log] = self.ancestors[self.ancestors[node][log - 1]][log - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for log in range(self.MAX_LOG - 1, -1, -1):
            if node == -1 or k == 0:
                break
            if k >= (1 << log):
                node = self.ancestors[node][log]
                k -= 1 << log

        return node