class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        box_range = {
            0: [0, 1, 2],
            1: [0, 1, 2],
            2: [0, 1, 2],
            3: [3, 4, 5],
            4: [3, 4, 5],
            5: [3, 4, 5],
            6: [6, 7, 8],
            7: [6, 7, 8],
            8: [6, 7, 8],
        }

        def markCell(x, y, n):
            if x > 8 or y > 8:
                return
            if x < 0 or y < 0:
                return

            for i in range(9):
                if board[i][y] == n or board[x][i] == n:
                    return False

            for i in box_range[x]:
                for j in box_range[y]:
                    if board[i][j] == n:
                        return False

            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] != ".":
                        continue

                    for n in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        valid = markCell(i, j, n)
                        if valid:
                            board[i][j] = n

                            solved = solve(board)
                            if solved:
                                return True
                            else:
                                board[i][j] = "."

                    return False

            return True

        solve(board)
