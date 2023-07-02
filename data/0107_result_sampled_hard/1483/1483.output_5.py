# @lc app=leetcode id=1483 lang=python3
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self.dp = [[-1] * 20 for _ in range(n)]  # 2^20 > 5 * 10^4

        for node in range(n):
            self.dp[node][0] = parent[node]

        for level in range(1, 20):
            for node in range(n):
                if self.dp[node][level - 1] != -1:
                    self.dp[node][level] = self.dp[self.dp[node][level - 1]][level - 1]

    def getKthAncestor(self, node: int, k: int) -> int:
        for level in range(20):
            if k & (1 << level):
                node = self.dp[node][level]
                if node == -1:
                    break

        return node