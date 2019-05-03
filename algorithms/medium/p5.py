# -*- coding: utf-8 -*-


class Solution:

    def check_order(self, n):
        m = n // 2
        i = 1
        yield m
        while m - i >= 0 or m + i < n:
            if m - i >= 0:
                yield m - i
            if m + i < n:
                yield m + i
            i += 1

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        result = ""
        for i in self.check_order(len(s)):
            if i < max_length // 2 or i >= len(s) - max_length // 2:
                break
            half_length = 1
            while i - half_length >= 0 and i + half_length < len(s):
                if s[i-half_length] != s[i+half_length]:
                    break
                half_length += 1
            half_length -= 1
            if 2 * half_length + 1 > max_length:
                max_length = 2 * half_length + 1
                result = s[i-half_length:i+half_length+1]
            half_length = 1
            while i - half_length + 1>= 0 and i + half_length < len(s):
                if s[i-half_length+1] != s[i+half_length]:
                    break
                half_length += 1
            half_length -= 1
            if 2 * half_length > max_length:
                max_length = 2 * half_length
                result = s[i-half_length+1:i+1+half_length]
        return result


if __name__ == '__main__':
    s = Solution()
    # assert s.longestPalindrome("babad") == "bab"
    assert s.longestPalindrome("cbbd") == "bb"
    assert s.longestPalindrome("") == ""
    assert s.longestPalindrome("abcdef") == "d"
    assert s.longestPalindrome("abababababababab") == "bababababababab"
    assert s.longestPalindrome("ab" * 10000) == "b" + "ab" * 9999
