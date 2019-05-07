# -*- coding: utf-8 -*-

"""
关键是要想明白最后一步不是删
因为长到短的删完全可以用短到长的增代替

这样增、换相关的只有3种情况
目标串少1，初始串少1，都少1

思路参考：https://blog.csdn.net/MebiuW/article/details/51420544
"""


class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)
        distance = [[0] * len(word2) for _ in word1]
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0:
                    if j == 0:
                        distance[i][j] = 0 if word1[i] == word2[j] else 1
                    else:
                        distance[i][j] = min(distance[i][j-1] + 1,
                                             j + (0 if word1[i] == word2[j] else 1))
                elif j == 0:
                    distance[i][j] = min(distance[i-1][j] + 1,
                                         i + (0 if word1[i] == word2[j] else 1))
                else:
                    distance[i][j] = min(distance[i-1][j] + 1,
                                         distance[i][j-1] + 1,
                                         distance[i-1][j-1] + (0 if word1[i] == word2[j] else 1))
        return distance[len(word1) - 1][len(word2) - 1]


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.minDistance("sea", "eat") == 2
    assert s.minDistance("plasma", "altruism") == 6
    # mine
    assert s.minDistance("horse", "ros") == 3
    assert s.minDistance("intention", "execution") == 5
    assert s.minDistance("", "") == 0
    assert s.minDistance("abc", "") == 3
    assert s.minDistance("", "abc") == 3
