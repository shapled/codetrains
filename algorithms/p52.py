# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def mark_it(self, n: int, mark: List[List[int]], i, j):
        for k in range(n):
            for l in range(n):
                if k == i:
                    mark[k][l] += 1
                if l == j:
                    mark[k][l] += 1
                if k + l == i + j:
                    mark[k][l] += 1
                if k - l == i - j:
                    mark[k][l] += 1

    def unmark_it(self, n: int, mark: List[List[int]], i, j):
        for k in range(n):
            for l in range(n):
                if k == i:
                    mark[k][l] -= 1
                if l == j:
                    mark[k][l] -= 1
                if k + l == i + j:
                    mark[k][l] -= 1
                if k - l == i - j:
                    mark[k][l] -= 1

    def DFS(self, n: int, line: int, mark: List[List[int]], solution):
        if line >= n:
            yield solution
            return
        for k, m in enumerate(mark[line]):
            if m == 0:
                self.mark_it(n, mark, line, k)
                yield from self.DFS(n, line+1, mark, solution + ((line, k), ))
                self.unmark_it(n, mark, line, k)

    def build_solution(self, n: int, solution):
        r = [["."] * n for _ in range(n)]
        for i, j in solution:
            r[i][j] = "Q"
        return ["".join(line) for line in r]

    def totalNQueens(self, n: int) -> int:
        ret = []
        mark = [[0] * n for _ in range(n)]
        for solution in self.DFS(n, 0, mark, ()):
            ret.append(self.build_solution(n, solution))
        return len(ret)


if __name__ == '__main__':
    s = Solution()
    assert s.totalNQueens(0) == 1
    assert s.totalNQueens(1) == 1
    assert s.totalNQueens(2) == 0
    assert s.totalNQueens(3) == 0
    assert s.totalNQueens(4) == 2
    assert s.totalNQueens(5) == 10
    assert s.totalNQueens(6) == 4
    assert s.totalNQueens(7) == 40
    assert s.totalNQueens(8) == 92
    assert s.totalNQueens(9) == 352
    assert s.totalNQueens(10) == 724
    assert s.totalNQueens(11) == 2680
