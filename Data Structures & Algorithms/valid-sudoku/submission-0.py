class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHash = defaultdict(set)
        colHash = defaultdict(set)
        cellHash = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[0])):
                cellIdx = ((r // 3) * 3) + (c // 3)
                num = board[r][c]
                if num != ".":
                    if num in rowHash[r] or num in colHash[c] or num in cellHash[cellIdx]:
                        print(num, cellIdx)
                        return False
                    rowHash[r].add(board[r][c])
                    colHash[c].add(board[r][c])
                    cellHash[cellIdx].add(board[r][c])
        return True