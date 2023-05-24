# @lc app=leetcode id=304 lang=python3
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.cumulative_sum = None
        else:
            rows, cols = len(matrix), len(matrix[0])
            self.cumulative_sum = [[0] * (cols + 1) for _ in range(rows + 1)]

            for i in range(1, rows + 1):
                for j in range(1, cols + 1):
                    self.cumulative_sum[i][j] = (
                        matrix[i - 1][j - 1]
                        + self.cumulative_sum[i - 1][j]
                        + self.cumulative_sum[i][j - 1]
                        - self.cumulative_sum[i - 1][j - 1]
                    )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.cumulative_sum:
            return 0

        return (
            self.cumulative_sum[row2 + 1][col2 + 1]
            - self.cumulative_sum[row2 + 1][col1]
            - self.cumulative_sum[row1][col2 + 1]
            + self.cumulative_sum[row1][col1]
        )