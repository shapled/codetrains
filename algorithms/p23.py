# -*- coding: utf-8 -*-

from typing import List


class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

    def __eq__(self, other):
        if not other or not isinstance(other, ListNode):
            return False
        i = self
        j = other
        while i.val == j.val:
            if i.next is None and j.next is None:
                return True
            if i.next is None or j.next is None:
                return False
            i = i.next
            j = j.next
        return False


class Solution:

    class NodeManager(object):

        def __init__(self, l: List[ListNode]):
            self.l = sorted(filter(None, l), key=lambda x: x.val)

        def pop_one(self):
            if len(self.l):
                return self.l.pop(0)
            return None

        def b_insert(self, l: List[ListNode], s: int, e: int, v: ListNode):
            if v.val <= l[s].val:
                self.l.insert(s, v)
                return
            if v.val >= l[e-1].val:
                self.l.insert(e, v)
                return
            m = (s + e) // 2
            if v.val > l[m].val:
                return self.b_insert(l, m, e, v)
            return self.b_insert(l, s, m, v)

        def add_one(self, v):
            if not self.l:
                self.l.append(v)
            else:
                self.b_insert(self.l, 0, len(self.l), v)

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        nm = Solution.NodeManager(lists)
        p = start = nm.pop_one()
        while p:
            if p.next:
                nm.add_one(p.next)
            last = p
            p = nm.pop_one()
            last.next = p
        return start


if __name__ == '__main__':
    s = Solution()
    L = ListNode
    assert s.mergeKLists([
        ListNode(1, ListNode(4, ListNode(5))),
        ListNode(1, ListNode(3, ListNode(4))),
        ListNode(2, ListNode(6)),
    ]) == ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4, ListNode(5, ListNode(6))))))))
    assert s.mergeKLists([L(1, L(2, L(4))), None]) == L(1, L(2, L(4)))