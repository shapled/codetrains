# -*- coding: utf-8 -*-

from typing import List


class Solution(object):

    def order_1_next(self, l1, l2):
        """ 增序 """
        i = 0
        j = 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                yield l1[i]
                i += 1
            else:
                yield l2[j]
                j += 1
        yield from l1[i:]
        yield from l2[j:]

    def order_2_next(self, l1, l2):
        """ 降序 """
        i = len(l1) - 1
        j = len(l2) - 1
        while i >= 0 and j >= 0:
            if l1[i] >= l2[j]:
                yield l1[i]
                i -= 1
            else:
                yield l2[j]
                j -= 1
        yield from l1[:i+1][::-1]
        yield from l2[:j+1][::-1]

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        o1 = self.order_1_next(nums1, nums2)
        o2 = self.order_2_next(nums1, nums2)
        v1 = next(o1)
        v2 = next(o2)
        while v1 < v2:
            v1 = next(o1)
            v2 = next(o2)
        return (v1 + v2) / 2


if __name__ == '__main__':
    s = Solution()
    assert 5.0 == s.findMedianSortedArrays([1, 3, 5, 7, 9], [2, 4, 5, 8])
    assert 3.0 == s.findMedianSortedArrays([3], [])
    assert 1.0 == s.findMedianSortedArrays([1, 1, 1, 1], [1])
