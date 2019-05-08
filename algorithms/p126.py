# -*- coding: utf-8 -*-

"""
这题广搜很好想到，但是时间一直超时
尝试了剪枝、双向广搜还是不行

参考别人做法后得知关键点在拼接新的字符串时不去遍历比较，而是直接生成判断是否存在
前者最坏 n^2 * size(word)，后者 26 * size(word)
在 6 个数以上时优化的效率很可观
"""

from typing import List


class Solution:
    chars = "abcdefghijklmnopqrstuvwxyz"

    def __init__(self):
        self.max_length = float("inf")
        self.min_pos = {}

    def match(self, s1: str, s2: str):
        cnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                cnt += 1
            if cnt > 1:
                return False
        return True

    def DBFS(self, begin: str, end: str, words: List[str]):
        b_words = set(words)
        e_words = (set(words) - {end}) | {begin}
        b_layers = [{begin: [(begin,)]}]
        e_layers = [{end: [(end,)]}]
        if end not in b_words:
            return []
        middle_words = set()
        while True:
            layer = {}
            for last in e_layers[-1]:
                # for word in e_words:
                    # if self.match(word, last):
                for i in range(len(last)):
                    for ch in self.chars:
                        word = last[:i] + ch + last[i+1:]
                        if word in e_words:
                            if word not in layer:
                                layer[word] = []
                            for path in e_layers[-1][last]:
                                layer[word].append(path + (word,))
            e_layers.append(layer)
            e_words -= set(layer)
            middle_words = set(e_layers[-1]) & set(b_layers[-1])
            if middle_words:
                break
            if not layer:
                break
            layer = {}
            for last in b_layers[-1]:
                # for word in b_words:
                #     if self.match(word, last):
                for i in range(len(last)):
                    for ch in self.chars:
                        word = last[:i] + ch + last[i+1:]
                        if word in b_words:
                            if word not in layer:
                                layer[word] = []
                            for path in b_layers[-1][last]:
                                layer[word].append(path + (word,))
            b_layers.append(layer)
            b_words -= set(layer)
            middle_words = set(e_layers[-1]) & set(b_layers[-1])
            if middle_words:
                break
            if not layer:
                break
        return self.build_path(b_layers, e_layers, middle_words)

    def build_path(self, b_layers, e_layers, middle_words):
        if not middle_words:
            return []
        ret = []
        for word in middle_words:
            for from_path in b_layers[-1][word]:
                for to_path in e_layers[-1][word]:
                    ret.append(list(from_path + to_path[::-1][1:]))
        return ret

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # deep = float("inf")
        # result = []
        # # for ret in self.DFS(beginWord, endWord, wordList, [beginWord]):
        # for ret in self.BFS(beginWord, endWord, wordList):
        #     if len(ret) < deep:
        #         deep = len(ret)
        #         result = [list(ret)]
        #     elif len(ret) == deep:
        #         result.append(list(ret))
        # return result
        return self.DBFS(beginWord, endWord, wordList)


if __name__ == '__main__':
    s = Solution()
    # error
    # assert s.findLadders("qa", "sq", [
    #     "si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar",
    #     "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma",
    #     "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge",
    #     "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh",
    #     "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be",
    #     "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"
    # ]) == [['qa', 'ca', 'cm', 'sm', 'sq'], ['qa', 'ca', 'ci', 'si', 'sq'], ['qa', 'ca', 'cr', 'sr', 'sq'],
    #        ['qa', 'ca', 'co', 'so', 'sq'], ['qa', 'ba', 'br', 'sr', 'sq'], ['qa', 'ba', 'bi', 'si', 'sq'],
    #        ['qa', 'ba', 'be', 'se', 'sq'], ['qa', 'ra', 're', 'se', 'sq'], ['qa', 'ra', 'rn', 'sn', 'sq'],
    #        ['qa', 'ra', 'rh', 'sh', 'sq'], ['qa', 'ra', 'rb', 'sb', 'sq'], ['qa', 'fa', 'fe', 'se', 'sq'],
    #        ['qa', 'fa', 'fr', 'sr', 'sq'], ['qa', 'fa', 'fm', 'sm', 'sq'], ['qa', 'ya', 'yo', 'so', 'sq'],
    #        ['qa', 'ya', 'yb', 'sb', 'sq'], ['qa', 'ya', 'ye', 'se', 'sq'], ['qa', 'ma', 'mt', 'st', 'sq'],
    #        ['qa', 'ma', 'mb', 'sb', 'sq'], ['qa', 'ma', 'me', 'se', 'sq'], ['qa', 'ma', 'mo', 'so', 'sq'],
    #        ['qa', 'ma', 'mn', 'sn', 'sq'], ['qa', 'ma', 'mi', 'si', 'sq'], ['qa', 'ma', 'mr', 'sr', 'sq'],
    #        ['qa', 'ga', 'go', 'so', 'sq'], ['qa', 'ga', 'ge', 'se', 'sq'], ['qa', 'ha', 'ho', 'so', 'sq'],
    #        ['qa', 'ha', 'hi', 'si', 'sq'], ['qa', 'ha', 'he', 'se', 'sq'], ['qa', 'na', 'nb', 'sb', 'sq'],
    #        ['qa', 'na', 'no', 'so', 'sq'], ['qa', 'na', 'ne', 'se', 'sq'], ['qa', 'na', 'ni', 'si', 'sq'],
    #        ['qa', 'la', 'ln', 'sn', 'sq'], ['qa', 'la', 'le', 'se', 'sq'], ['qa', 'la', 'lt', 'st', 'sq'],
    #        ['qa', 'la', 'lo', 'so', 'sq'], ['qa', 'la', 'li', 'si', 'sq'], ['qa', 'la', 'lr', 'sr', 'sq'],
    #        ['qa', 'ta', 'tm', 'sm', 'sq'], ['qa', 'ta', 'ti', 'si', 'sq'], ['qa', 'ta', 'to', 'so', 'sq'],
    #        ['qa', 'ta', 'tc', 'sc', 'sq'], ['qa', 'ta', 'th', 'sh', 'sq'], ['qa', 'ta', 'tb', 'sb', 'sq'],
    #        ['qa', 'pa', 'ph', 'sh', 'sq'], ['qa', 'pa', 'po', 'so', 'sq'], ['qa', 'pa', 'pb', 'sb', 'sq'],
    #        ['qa', 'pa', 'pm', 'sm', 'sq'], ['qa', 'pa', 'pi', 'si', 'sq'], ['qa', 'pa', 'pt', 'st', 'sq']]
    assert s.findLadders("hot", "dog", ["hot", "dog"]) == []
    # mine
    assert s.findLadders("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) == \
           [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
    assert s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"]) == []
    assert s.findLadders("abc", "def", ["aef"]) == []
