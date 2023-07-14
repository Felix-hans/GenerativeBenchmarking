# @lc app=leetcode id=119 lang=python3
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # Initialize the first row
        
        for i in range(rowIndex):
            next_row = [1]  # First element of the row is always 1
            
            for j in range(1, len(row)):
                next_row.append(row[j-1] + row[j])
            
            next_row.append(1)  # Last element of the row is always 1
            row = next_row  # Update the current row
        
        return row