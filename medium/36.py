from typing import List

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = []
        box = []

        for i in range(len(board)):
            for y in range(len(board)):
                if board[i][y] != '.':
                    s += [(i, board[i][y]), (board[i][y], y)]
                    box += [(i // 3, y // 3, board[i][y])]

        return len(box) == len(set(box)) and len(s) == len(set(s))

res = Solution().isValidSudoku(board=board)
print(res)