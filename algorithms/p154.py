# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def bsearch(self, nums: List[int], start, end) -> int:
        """
        start < middle < end => start
        start < middle > end => [middle, end]
        start < middle = end => [start, middle]
        start > middle < end => [start, middle]
        start > middle > end => X
        start > middle = end => [start, middle]
        start = middle > end => [middle, end]
        start = middle < end => start
        start = middle = end => 重置 start / middle，都失败返回 start
        """
        if start == end:
            return nums[start]
        if start + 1 == end:
            return min(nums[start], nums[end])
        middle = (start + end) // 2
        if nums[start] < nums[middle] < nums[end]:
            return nums[start]
        elif nums[start] < nums[middle] > nums[end]:
            return self.bsearch(nums, middle, end)
        elif nums[start] < nums[middle] == nums[end]:
            return self.bsearch(nums, start, middle)
        elif nums[start] > nums[middle] < nums[end]:
            return self.bsearch(nums, start, middle)
        elif nums[start] > nums[middle] > nums[end]:
            return 0
        elif nums[start] > nums[middle] == nums[end]:
            return self.bsearch(nums, start, middle)
        elif nums[start] == nums[middle] > nums[end]:
            return self.bsearch(nums, middle, end)
        elif nums[start] == nums[middle] < nums[end]:
            return nums[start]
        elif nums[start] == nums[middle] == nums[end]:
            while start < middle and nums[start] == nums[middle]:
                start += 1
            if start < middle:
                return self.bsearch(nums, start, end)
            while middle < end and nums[middle] == nums[end]:
                middle += 1
            if middle < end:
                return self.bsearch(nums, middle, end)
            return nums[start]

    def findMin(self, nums: List[int]) -> int:
        return self.bsearch(nums, 0, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    assert s.findMin([1, 3, 5]) == 1
    assert s.findMin([2, 2, 2, 0, 1]) == 0
    assert s.findMin([100] * 100 + [99] + [100] * 100) == 99
    assert s.findMin([100] * 100 + [101] + [100] * 100) == 100
    assert s.findMin([-3]) == -3
