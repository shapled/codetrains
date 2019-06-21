# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        steps = [float("inf")] * len(nums)
        steps[0] = 0
        for i in range(len(nums) - 1):
            if i > 0 and (nums[i-1]-nums[i]) == 1:
                continue
            for j in range(1, nums[i]+1):
                if i + j >= len(nums):
                    break
                steps[i + j] = min(steps[i] + 1, steps[i + j])
                if i + j == len(nums) - 1:
                    return int(steps[-1])
        return int(steps[-1])


if __name__ == '__main__':
    s = Solution()
    # error
    l = list(range(25000, -1, -1))
    l.insert(-2, 1)
    assert s.jump(l) == 2
    # mine
    assert s.jump([2, 3, 1, 1, 4]) == 2
    assert s.jump([1]) == 0
    assert s.jump([3, 2, 4, 1, 0, 1, 4, 5, 6, 8, 1]) == 3
