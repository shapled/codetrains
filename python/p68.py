# -*- coding: utf-8 -*-

from typing import List


class Solution:

    def expand(self, line, width):
        if len(line) == 1:
            return line[0] + " " * (width - len(line[0]))
        n = len(line) - 1
        d, m = divmod(width - sum(map(len, line)), n)
        ret = []
        for i, word in enumerate(line):
            ret.append(word)
            if i < len(line) - 1:
                ret.append(" " * ((d + 1) if i < m else d))
        return "".join(ret)

    def left_justify_line(self, line, width):
        s = " ".join(line)
        return s + " " * (width - len(s))

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        line = []
        for word in words:
            if sum(map(len, line)) + len(line) + len(word) > maxWidth:
                lines.append(line)
                line = [word]
            else:
                line.append(word)
        if line:
            lines.append(line)
        ret = [self.expand(l, maxWidth) for l in lines[:-1]] + [self.left_justify_line(lines[-1], maxWidth)]
        return ret


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16) == [
        "What   must   be", "acknowledgment  ", "shall be        "]
    # mine
    assert s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16) == \
           ["This    is    an", "example  of text", "justification.  "]
    assert s.fullJustify(["abc"], 3) == ["abc"]
    assert s.fullJustify(["def", "ab"], 3) == ["def", "ab "]
