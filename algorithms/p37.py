# -*- coding: utf-8 -*-

from typing import List


class Solution:
    blocks = {
        0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2],
        3: [3, 4, 5], 4: [3, 4, 5], 5: [3, 4, 5],
        6: [6, 7, 8], 7: [6, 7, 8], 8: [6, 7, 8],
    }
    all_pos = [(i, j) for i in range(9) for j in range(9)]

    def avaliable_number(self, board, i, j):
        numbers = set(map(str, range(1, 10)))
        for number in board[i]:
            numbers -= {number}
        for line in board:
            for number in line[j]:
                numbers -= {number}
        for ii in self.blocks[i]:
            for jj in self.blocks[j]:
                number = board[ii][jj]
                numbers -= {number}
        return numbers

    def calculate(self, board: List[List[str]]):
        is_full = True
        for i, j in self.all_pos:
            if board[i][j] == ".":
                if_full = False
                for n in self.avaliable_number(board, i, j):
                    board[i][j] = n
                    if self.calculate(board):
                        return True
                    board[i][j] = "."
                return False
        return is_full

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.calculate(board)


if __name__ == '__main__':
    s = Solution()
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    s.solveSudoku(board)
    assert board == [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'],
                     ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'],
                     ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'],
                     ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'],
                     ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    board = [["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9, ["."] * 9]
    s.solveSudoku(board)
    for i, j in s.all_pos:
        assert not s.avaliable_number(board, i, j)
