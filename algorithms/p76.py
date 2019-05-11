# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, pos=None, prev=None, nxt=None):
        self.prev = prev
        self.next = nxt
        self.pos = pos


class Solution:
    def count_of_t(self, t: str):
        r = {}
        for s in t:
            r[s] = r.get(s, 0) + 1
        return r

    def minWindow(self, s: str, t: str) -> str:
        head = tail = Node()
        result = ""
        char_to_node = {}
        full = False
        litters = self.count_of_t(t)
        for i, char in enumerate(s):
            if char not in litters:
                continue
            if char not in char_to_node:
                char_to_node[char] = []
            if len(char_to_node[char]) == litters[char]:
                node = char_to_node[char].pop(0)
                # 移除 node
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    tail = node.prev
            # 创建新 node
            node = Node(i)
            tail.next = node
            node.prev = tail
            tail = node
            char_to_node[char].append(node)
            if full or all([litters[c] == len(char_to_node.get(c, [])) for c in litters]):
                full = True
                if (not result) or (tail.pos + 1 - head.next.pos < len(result)):
                    result = s[head.next.pos:tail.pos+1]
        return result


if __name__ == '__main__':
    s = Solution()
    # error
    assert s.minWindow("a", "aa") == ""
    # mine
    assert s.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert s.minWindow("ADMOBECOTDEBANC", "ABCDD") == "ADMOBECOTD"
    assert s.minWindow("", "ABC") == ""
    assert s.minWindow("DOBECODEBNC", "ABC") == ""
    assert s.minWindow("", "") == ""
    assert s.minWindow("ADOBECODEBANC", "") == ""
