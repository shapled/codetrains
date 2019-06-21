# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def search_and_insert(self, l: List[int], start: int, end: int, v: int):
        if start > end:
            l.insert(start, v)
            return start
        if v <= l[start]:
            l.insert(start, v)
            return start
        if v > l[end]:
            l.insert(end+1, v)
            return end + 1
        if start + 1 >= end:
            l.insert(start+1, v)
            return start + 1
        middle = (start + end) // 2
        if l[start] < v <= l[middle]:
            return self.search_and_insert(l, start, middle-1, v)
        return self.search_and_insert(l, middle, end, v)

    def countSmaller(self, nums: List[int]) -> List[int]:
        ret = []
        l = []
        for i in range(len(nums)-1, -1, -1):
            ret.append(self.search_and_insert(l, 0, len(l)-1, nums[i]))
        return ret[::-1]


if __name__ == '__main__':
    s = Solution()
    assert s.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
    assert s.countSmaller([]) == []
    assert s.countSmaller([-1]) == [0]
    assert s.countSmaller(list(range(1000))) == [0] * 1000
    assert s.countSmaller([2, 0, 1]) == [2, 0, 0]
