# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """ 按照括号匹配相同的思路做就行了 """
        ret = 0
        changed = True
        while changed:
            changed = False
            i = 1
            left = -1
            while i < len(height):
                if height[i-1] > height[i]:
                    left = i - 1
                elif height[i-1] == height[i]:
                    pass
                else:  # <
                    if left != -1:
                        to = min(height[left], height[i])
                        for j in range(left+1, i):
                            ret += to - height[j]
                            height[j] = to
                        if to == height[left]:
                            left = -1
                        changed = True
                i += 1
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert s.trap([]) == 0
    assert s.trap([0, 0, 0]) == 0
    assert s.trap([0, 6, 2, 3, 4]) == 3
    assert s.trap([1, 1, 1]) == 0
    assert s.trap([3, 1, 1, 5, 0, 4, 8, 1, 1]) == 10
