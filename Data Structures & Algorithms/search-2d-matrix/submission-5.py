class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, lCol,rRow, rCol = 0,0, len(matrix) - 1, len(matrix[0]) - 1
        row = -1
        while lRow <= rRow:
            midRow = lRow + (rRow - lRow) // 2
            if matrix[midRow][0] == target or matrix[midRow][-1] == target:
                return True
            elif matrix[midRow][0] < target and matrix[midRow][-1] > target:
                row = midRow
                break
            elif matrix[midRow][0] < target:
                lRow = midRow + 1
            else:
                rRow = midRow - 1
        if row == -1:
            return False
        while lCol <= rCol:
            midCol = lCol + (rCol - lCol) // 2
            if matrix[row][midCol] == target:
                return True
            elif matrix[row][midCol] < target:
                lCol = midCol + 1
            else:
                rCol = midCol - 1
        return False