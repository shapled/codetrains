# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def pos_of_max(self, l: List[int]):
        pos = -1
        max_v = -float("inf")
        for i, value in enumerate(l):
            if value >= max_v:
                max_v = value
                pos = i
        return pos

    def maxProfit(self, prices: List[int]) -> int:
        first = [0] * len(prices)
        second = [0] * len(prices)
        min_buy = float("inf")
        i = 0
        while i < len(prices):
            if min_buy > prices[i]:
                min_buy = prices[i]
            first[i] = prices[i] - min_buy
            i += 1
        max_sell = -float("inf")
        i = len(prices) - 1
        while i >= 0:
            if max_sell < prices[i]:
                max_sell = prices[i]
            second[i] = max_sell - prices[i]
            i -= 1
        i = 0
        result = 0
        while i < len(prices):
            j = self.pos_of_max(second[i:])  # j 不可能是 -1
            k = self.pos_of_max(first[:i+j])  # k 可能是 -1
            s = second[i+j] if j != -1 else 0
            f = first[k] if k != -1 else 0
            if s + f > result:
                result = s + f
            i = i + j + 1
        return result


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.maxProfit(list(range(10000, 540, -1)) + [539, 541, 540, 542] + list(range(539, -1, -1)) + [0]*16000) == 4
    assert s.maxProfit([3, 2, 6, 5, 0, 3]) == 7
    # mine
    assert s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]) == 6
    assert s.maxProfit([1, 2, 3, 4, 5]) == 4
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
    assert s.maxProfit([]) == 0
    assert s.maxProfit(list(range(0, 10000))[::-1]) == 0
