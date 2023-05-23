# @lc app=leetcode id=119 lang=python3
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Initialize the row with the first element as 1
        for i in range(1, rowIndex + 1):
            next_row = [1]  # Start the next row with 1
            for j in range(1, i):
                next_row.append(row[j - 1] + row[j])  # Sum of two adjacent elements in the previous row
            next_row.append(1)  # End the next row with 1
            row = next_row  # Update the current row with the next row
        return row