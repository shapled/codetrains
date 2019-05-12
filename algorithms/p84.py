# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def find_next_less_than(self, l: List[int], than: int, start=0):
        eq = []
        for i, v in enumerate(l[start:]):
            if v < than:
                return i + start, eq
            if v == than:
                eq.append(start + i)
        return None, eq

    def next_turn_start(self, n: int, pos_set):
        for k in range(n):
            if k in pos_set:
                return k
        return None

    def next_turn_end(self, n: int, pos_set):
        for k in range(n-1, -1, -1):
            if k in pos_set:
                return k
        return None

    def scan_once(self, start: int, heights: List[int], pos_set: set):
        i = start
        max_area = 0
        while True:
            pos_set.remove(i)
            height = heights[i]
            j, eq = self.find_next_less_than(heights, height, i + 1)
            for p in eq:
                if p in pos_set:
                    pos_set.remove(p)
            if (j is None) or (j not in pos_set):  # 这一轮结束
                width = (len(heights) if j is None else j) - start
                max_area = max(max_area, width * height)
                break
            else:
                width = j - start
                max_area = max(max_area, width * height)
                i = j
        return max_area

    def reverse_scan_once(self, end: int, heights: List[int], pos_set: set):
        start = len(heights) - 1 - end
        heights = heights[::-1]
        i = start
        max_area = 0
        while True:
            pos_set.remove(len(heights) - 1 - i)
            height = heights[i]
            j, eq = self.find_next_less_than(heights, height, i + 1)
            for p in eq:
                if (len(heights) - 1 - p) in pos_set:
                    pos_set.remove(len(heights) - 1 - p)
            if (j is None) or (len(heights) - 1 - j not in pos_set):  # 这一轮结束
                width = (len(heights) if j is None else j) - start
                max_area = max(max_area, width * height)
                break
            else:
                width = j - start
                max_area = max(max_area, width * height)
                i = j
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        max_area = 0
        pos_set = set(range(len(heights)))  # 未计算的起点
        while True:
            if not pos_set:
                break
            start = self.next_turn_start(len(heights), pos_set)
            max_area = max(max_area, self.scan_once(start, heights, pos_set))
            if not pos_set:
                break
            end = self.next_turn_end(len(heights), pos_set)
            max_area = max(max_area, self.reverse_scan_once(end, heights, pos_set))
        return max_area


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.largestRectangleArea([0, 2, 0]) == 2
    assert s.largestRectangleArea([1] * 10000) == 10000
    assert s.largestRectangleArea([1]) == 1
    # mine
    assert s.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
    assert s.largestRectangleArea([]) == 0
    assert s.largestRectangleArea(list(range(1, 10001))) == 25005000
