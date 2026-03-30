class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lRow, lCol,rRow, rCol = 0,0, len(matrix) - 1, len(matrix[0]) - 1
        while lRow <= rRow:
            midRow = lRow + (rRow - lRow) // 2
            if matrix[midRow][0] == target or matrix[midRow][-1] == target:
                return True
            elif matrix[midRow][0] < target and matrix[midRow][-1] > target:
                break
            elif matrix[midRow][0] < target and matrix[midRow][-1] < target:
                lRow = midRow + 1
            else:
                rRow = midRow - 1
        while lCol <= rCol:
            midCol = lCol + (rCol - lCol) // 2
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] < target:
                lCol = midCol + 1
            else:
                rCol = midCol - 1
        return False