# -*- coding: utf-8 -*-


class Solution:
    ANY_CHAR = 0
    ANY_CHARS = 1
    CERTAIN_CHAR = 2
    CERTAIN_CHARS = 3

    def DFS(self, s, p, s_pos, p_pos):
        if p_pos >= len(p):
            return s_pos >= len(s)
        e = p[p_pos]
        if e[0] == self.ANY_CHAR:
            if not self.skip_char(s, s_pos):
                return False
            return self.DFS(s, p, s_pos+1, p_pos+1)
        elif e[0] == self.ANY_CHARS:
            for n in range(self.get_count_of_char(s, s_pos) + 1):
                if not self.skip_n_chars(s, s_pos, n):
                    continue
                if self.DFS(s, p, s_pos+n, p_pos+1):
                    return True
            return False
        elif e[0] == self.CERTAIN_CHAR:
            if not self.skip_char(s, s_pos, e[1]):
                return False
            return self.DFS(s, p, s_pos+1, p_pos+1)
        else:  # self.CERTAIN_CHARS
            for n in range(self.get_count_of_char(s, s_pos, e[1]) + 1):
                if not self.skip_n_chars(s, s_pos, n, e[1]):
                    continue
                if self.DFS(s, p, s_pos+n, p_pos+1):
                    return True
            return False

    def get_count_of_char(self, s: str, start_pos: int, char: str = None):
        if not char:
            return max(len(s) - start_pos, 0)
        cnt = 0
        while start_pos < len(s):
            if s[start_pos] != char:
                break
            cnt += 1
            start_pos += 1
        return cnt

    def skip_char(self, s: str, pos: int, char: str = None):
        return self.skip_n_chars(s, pos, 1, char)

    def skip_n_chars(self, s: str, pos: int, n: int, char: str = None):
        if pos + n - 1 >= len(s):
            return False
        if char:
            i = 0
            while i < n:
                if s[pos + i] != char:
                    return False
                i += 1
            return True
        return True

    def normalize_pattern(self, p: str):
        new_p = []
        i = 0
        while i < len(p):
            if p[i] == ".":
                if (i + 1) < len(p) and p[i+1] == "*":
                    if len(new_p) == 0 or new_p[-1][0] != self.ANY_CHARS or new_p[-1][1] != p[i]:
                        new_p.append((self.ANY_CHARS, p[i]))
                else:
                    new_p.append((self.ANY_CHAR, p[i]))
            elif p[i] == "*":
                pass
            else:
                if (i + 1) < len(p) and p[i+1] == "*":
                    if len(new_p) == 0 or new_p[-1][0] != self.CERTAIN_CHARS or new_p[-1][1] != p[i]:
                        new_p.append((self.CERTAIN_CHARS, p[i]))
                else:
                    new_p.append((self.CERTAIN_CHAR, p[i]))
            i += 1
        return new_p

    def isMatch(self, s: str, p: str) -> bool:
        pattern = self.normalize_pattern(p)
        return self.DFS(s, pattern, 0, 0)


if __name__ == '__main__':
    s = Solution()
    # error:
    assert not s.isMatch("aaaaabaccbbccababa", "a*b*.*c*c*.*.*.*c")
    assert not s.isMatch("mississippi", "mis*is*p*.")
    # mine:
    assert s.isMatch("abc", ".*")
    assert not s.isMatch("abc", ".")
    assert not s.isMatch("abc", "*")  # * 开头应该理解为空串，跳过
    assert s.isMatch("abc", "a.c.*")
    assert not s.isMatch("ac", "a.c.*")
    assert not s.isMatch("abc", "a.c..*")
    # 没有转义符，不需要支持转义
    assert s.isMatch("aaaa", "a*")
    assert s.isMatch("abbac", "c*ab*a*c")
    # a** 的含义呢？ 应该和 a* 是等价的
    assert s.isMatch("abc", "a**bcd**")
    assert s.isMatch("aaabc", "a*abc")  # pattern 处理的时候应该合并 a*a
    assert s.isMatch("aaabc", ".*abc")  # 也需要合并 .*a
    assert s.isMatch("babacac", ".*ac")  # 这种也要处理
    assert s.isMatch("babacac", ".*acac")
    assert s.isMatch("babacabac", ".*bac")
    # 应该用深搜的思路去做，.* 可以匹配0个，1个，2个 ...
