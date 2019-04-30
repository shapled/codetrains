# -*- coding: utf-8 -*-


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        """ 移除法 """
        mark = list(s)
        changed = True
        while changed:
            i = 0
            last = 0
            last_i = -1
            changed = False
            while i < len(mark):
                if last == 0:
                    if mark[i] == "(":
                        last = mark[i]
                        last_i = i
                else:
                    if mark[i] == 0:
                        pass
                    elif mark[i] == last:
                        last_i = i
                    else:
                        mark[i] = 0
                        mark[last_i] = 0
                        last = 0
                        last_i = -1
                        changed = True
                i += 1
        longest = 0
        current = 0
        for v in mark:
            if v == 0:
                current += 1
            else:
                longest = current if longest < current else longest
                current = 0
        longest = current if longest < current else longest
        return longest


if __name__ == '__main__':
    s = Solution()
    assert s.longestValidParentheses("(()") == 2
    assert s.longestValidParentheses(")()())") == 4
    assert s.longestValidParentheses("(((") == 0
    assert s.longestValidParentheses(")()()(()(()()()((())()))") == 18
    assert s.longestValidParentheses("") == 0
    assert s.longestValidParentheses("()") == 2
