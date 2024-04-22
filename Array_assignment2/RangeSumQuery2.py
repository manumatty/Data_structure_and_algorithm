#https://leetcode.com/problems/range-sum-query-2d-immutable/
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # Initialize the sum matrix with one extra row and column for storing prefix sums
        rowLength, colLength = len(matrix), len(matrix[0])
        self.sumMat = [[0] * (colLength + 1) for rows in range(rowLength + 1)]
        
        for row in range(rowLength):
            # Initialize prefix sum for the current row
            prefixSum = 0
            for col in range(colLength):
                # Add the current element to the prefix sum
                prefixSum += matrix[row][col]
                # Store the prefix sum in the sum matrix
                above = self.sumMat[row][col + 1]
                self.sumMat[row + 1][col + 1] = prefixSum + above
                
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Add 1 to row and column indices to match the sum matrix indices
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        # Calculate the sum of the region using the sum matrix
        bottomRight = self.sumMat[row2][col2]
        above = self.sumMat[row1 - 1][col2]
        left = self.sumMat[row2][col1 - 1]
        topLeft = self.sumMat[row1 - 1][col1 - 1]
        
        return bottomRight - above - left + topLeft 