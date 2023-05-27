# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix_sums = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.prefix_sums = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.prefix_sums[i][j] = (
                        matrix[i - 1][j - 1]
                        + self.prefix_sums[i - 1][j]
                        + self.prefix_sums[i][j - 1]
                        - self.prefix_sums[i - 1][j - 1]
                    )

    def sumRegion(self, row1, col1, row2, col2):
        if self.prefix_sums is None:
            return 0

        return (
            self.prefix_sums[row2 + 1][col2 + 1]
            - self.prefix_sums[row1][col2 + 1]
            - self.prefix_sums[row2 + 1][col1]
            + self.prefix_sums[row1][col1]
        )