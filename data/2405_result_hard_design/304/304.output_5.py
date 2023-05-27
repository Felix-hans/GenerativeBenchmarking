# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.cumulative_sum = None
        else:
            m, n = len(matrix), len(matrix[0])
            self.cumulative_sum = [[0] * (n + 1) for _ in range(m + 1)]

            for i in range(1, m + 1):
                for j in range(1, n + 1):
                    self.cumulative_sum[i][j] = (
                        matrix[i - 1][j - 1]
                        + self.cumulative_sum[i - 1][j]
                        + self.cumulative_sum[i][j - 1]
                        - self.cumulative_sum[i - 1][j - 1]
                    )

    def sumRegion(self, row1, col1, row2, col2):
        if self.cumulative_sum is None:
            return 0

        return (
            self.cumulative_sum[row2 + 1][col2 + 1]
            - self.cumulative_sum[row2 + 1][col1]
            - self.cumulative_sum[row1][col2 + 1]
            + self.cumulative_sum[row1][col1]
        )