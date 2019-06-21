# -*- coding: utf-8 -*-

from typing import List


class Node(object):
    def __init__(self, value=None):
        self.children = {}
        self.value = value


class Solution:

    def build_trie_tree(self, words: List[str]):
        root = Node()
        for word in words:
            curr = root
            for char in word:
                if char not in curr.children:
                    curr.children[char] = Node()
                curr = curr.children[char]
            curr.value = word
        return root

    def match(self, board: List[List[str]], pos: (int, int), node: Node, path: List):
        if node.value:
            yield "".join([board[a][b] for a, b in path])
        m = len(board)
        n = len(board[0])
        i, j = pos
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        char = board[i][j]
        if char in node.children:
            path.append((i, j))
            node = node.children[char]
            sp = set(path)
            for a, b in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if (a, b) not in sp:
                    yield from self.match(board, (a, b), node, path)
            path.pop()
        return

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board:
            return []
        root = self.build_trie_tree(words)
        ret = set()
        for i, line in enumerate(board):
            for j, char in enumerate(line):
                for word in self.match(board, (i, j), root, []):
                    ret.add(word)
        return list(ret)


if __name__ == '__main__':
    s = Solution()
    assert s.findWords(board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
],
words = ["oath","pea","eat","rain"]) == ["eat","oath"]
    assert s.findWords([], []) == []
    assert s.findWords([], ["a"]) == []
    assert s.findWords([["a"]], []) == []
    assert s.findWords([["a", "b"], ["c", "d"]], ["abdc", "abdca"]) == ["abdc"]
    assert s.findWords([["a", "b"], ["c", "d"], ["a", "b"]], ["abdc", "abdca"]) == ["abdc", "abdca"]
