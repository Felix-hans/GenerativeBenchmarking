# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefixSum = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.prefixSum = [[0] * (n + 1) for _ in range(m + 1)]
            
            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.prefixSum[i][j] = (
                        matrix[i-1][j-1]
                        + self.prefixSum[i-1][j]
                        + self.prefixSum[i][j-1]
                        - self.prefixSum[i-1][j-1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.prefixSum is None:
            return 0

        return (
            self.prefixSum[row2+1][col2+1]
            - self.prefixSum[row1][col2+1]
            - self.prefixSum[row2+1][col1]
            + self.prefixSum[row1][col1]
        )