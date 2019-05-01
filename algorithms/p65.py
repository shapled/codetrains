# -*- coding: utf-8 -*-


class Solution:
    numbers = set("0123456789")
    valid_chars = set("0123456789e+-.")

    def check_chars(self, s: str):
        if not s:
            return False
        for char in s:
            if char not in self.valid_chars:
                return False
        return True

    def is_digits(self, s: str):
        if not s:
            return False
        for char in s:
            if char not in self.numbers:
                return False
        return True

    def is_int(self, s: str):
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]
        return self.is_digits(s)

    def is_float(self, s: str):
        if s.startswith("+") or s.startswith("-"):
            s = s[1:]
        parts = s.split(".")
        if not len(parts) == 2:
            return False
        left, right = parts
        if ((not left) and self.is_digits(right)) \
                or (self.is_int(left) and (not right)) \
                or (self.is_int(left) and self.is_digits(right)):
            return True
        return False

    def is_e(self, s: str):
        parts = s.split("e")
        if not len(parts) == 2:
            return False
        left, right = parts
        if (self.is_float(left) or self.is_int(left)) and self.is_int(right):
            return True
        return False

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not self.check_chars(s):
            return False
        if self.is_int(s) or self.is_float(s) or self.is_e(s):
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.isNumber("+.8")

    # mine
    assert s.isNumber("0")
    assert s.isNumber(" 0.1 ")
    assert not s.isNumber("abc")
    assert not s.isNumber("1 a")
    assert s.isNumber("2e10")
    assert s.isNumber(" -90e3    ")
    assert not s.isNumber(" 1e")
    assert not s.isNumber("e3")
    assert s.isNumber(" 6e-1")
    assert not s.isNumber(" 99e2.5")
    assert s.isNumber("53.5e93")
    assert not s.isNumber(" --6 ")
    assert not s.isNumber("-+3")
    assert not s.isNumber("95a54e53")

    assert s.isNumber(".1")
    assert s.isNumber("3e0")
    assert s.isNumber("+03")
    assert not s.isNumber("- 3")
