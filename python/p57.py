# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        na, nb = newInterval
        left = None
        merged = False
        for a, b in intervals:
            if merged:  # 已处理，不用比较了
                ret.append([a, b])
            elif nb < a:  # 新的在左边
                left = na if left is None else left
                ret.append([left, nb])
                ret.append([a, b])
                merged = True
            elif na < a <= nb <= b:
                left = na if left is None else left
                ret.append([left, b])
                merged = True
            elif na < a <= b < nb:
                left = na if left is None else left
            elif a <= na <= nb <= b:
                ret.append([a, b])
                merged = True
            elif a <= na <= b < nb:
                left = a
            elif b < na:
                ret.append([a, b])
        if not merged:
            left = na if left is None else left
            ret.append([left, nb])
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert s.insert([], [2, 3]) == [[2, 3]]
    assert s.insert([[1, 2]], [3, 4]) == [[1, 2], [3, 4]]
    assert s.insert([[3, 4]], [1, 2]) == [[1, 2], [3, 4]]
    assert s.insert([[1, 5], [8, 9]], [6, 7]) == [[1, 5], [6, 7], [8, 9]]
    assert s.insert([[3, 5], [8, 9]], [1, 2]) == [[1, 2], [3, 5], [8, 9]]
    assert s.insert([[1, 5], [6, 7]], [8, 9]) == [[1, 5], [6, 7], [8, 9]]
