# -*- coding: utf-8 -*-


def cache(func):
    def _inner(instance, s, p, s_pos, p_pos):
        if (s_pos, p_pos) not in Solution.r:
            Solution.r[s_pos, p_pos] = func(instance, s, p, s_pos, p_pos)
        return Solution.r[s_pos, p_pos]
    return _inner


class Solution:
    ANY_CHAR = 0
    ANY_CHARS = 1
    CERTAIN_CHAR = 2
    r = {}

    def skip_char(self, s: str, pos: int, char: str = None):
        if pos >= len(s):
            return False
        if char and s[pos] != char:
            return False
        return True

    def normalize_pattern(self, p):
        pattern = []
        for char in p:
            if char == "?":
                pattern.append((self.ANY_CHAR, "?"))
            elif char == "*":
                if (not pattern) or (pattern[-1][0] != self.ANY_CHARS):
                    pattern.append((self.ANY_CHARS, "*"))
            else:
                pattern.append((self.CERTAIN_CHAR, char))
        return pattern

    @cache
    def DFS(self, s, p, s_pos, p_pos):
        if p_pos >= len(p):
            return s_pos >= len(s)
        pattern = p[p_pos]
        if pattern[0] == self.ANY_CHAR:
            if not self.skip_char(s, s_pos):
                return False
            return self.DFS(s, p, s_pos+1, p_pos+1)
        elif pattern[0] == self.CERTAIN_CHAR:
            if not self.skip_char(s, s_pos, pattern[1]):
                return False
            return self.DFS(s, p, s_pos+1, p_pos+1)
        else:  # ANY_CHARS
            for n in range(len(s) - s_pos + 1):
                if self.DFS(s, p, s_pos+n, p_pos+1):
                    return True
            return False

    def isMatch(self, s: str, p: str) -> bool:
        """ 这和 . * 的正则基本一样，正好再敲一遍 """
        Solution.r = {}
        pattern = self.normalize_pattern(p)
        return self.DFS(s, pattern, 0, 0)


if __name__ == '__main__':
    s = Solution()
    # error
    # assert not s.isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbb"
    #                      "bbbbbbaabbb", "b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a")
    # mine
    # assert not s.isMatch("aa", "a")
    assert s.isMatch("aa", "*")
    assert not s.isMatch("cb", "?a")
    assert s.isMatch("adceb", "*a*b")
    assert not s.isMatch("acdcb", "a*c?b")
    assert s.isMatch("", "")
    assert s.isMatch("", "*")
