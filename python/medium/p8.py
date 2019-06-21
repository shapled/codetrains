# -*- coding: utf-8 -*-

class Solution:
    digits = set("0123456789")
    min_v = -2 ** 31
    max_v = 2 ** 31 - 1

    def extract_number(self, s: str):
        r = []
        if s.startswith("+") or s.startswith("-"):
            r.append(s[0])
            s = s[1:]
        if not (s and s[0] in self.digits):
            return 0
        for char in s:
            if char in self.digits:
                r.append(char)
            else:
                break
        return int("".join(r))

    def change_to_range(self, n: int):
        return max(min(n, self.max_v), self.min_v)

    def myAtoi(self, str: str) -> int:
        number = self.extract_number(str.lstrip())
        ret = self.change_to_range(number)
        return ret


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi("42") == 42
    assert s.myAtoi("   -42") == -42
    assert s.myAtoi("4193 with words") == 4193
    assert s.myAtoi("words and 987") == 0
    assert s.myAtoi("-91283472332") == -2147483648
    assert s.myAtoi("") == 0
    assert s.myAtoi("+") == 0
    assert s.myAtoi(str(2**31)) == 2 ** 31 - 1
    assert s.myAtoi(str(2**31 - 1)) == 2 ** 31 - 1
    assert s.myAtoi(str(-2**31)) == - 2 ** 31
    assert s.myAtoi(str(-2**31-1)) == - 2 ** 31

