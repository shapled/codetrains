# -*- coding: utf-8 -*-

class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt

    def __eq__(self, other):
        p = self
        q = other
        while p and q:
            if p.val != q.val:
                return False
            p = p.next
            q = q.next
        if p is not None or q is not None:
            return False
        return True

    def __str__(self):
        curr = self
        ret = []
        while curr:
            ret.append(str(curr.val))
            curr = curr.next
        return "<" + ",".join(ret) + ">"

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr = start = None
        s = 0
        while l1 or l2:
            if curr is None:
                curr = start = ListNode(0)
            else:
                curr.next = ListNode(0)
                curr = curr.next
            s = (l1.val if l1 else 0) + (l2.val if l2 else 0) + s//10
            curr.val = s % 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if s >= 10:
            curr.next = ListNode(s // 10)
        return start


if __name__ == '__main__':
    s = Solution()
    L = ListNode
    assert s.addTwoNumbers(L(2, L(4, L(3))), L(5, L(6, L(4)))) == L(7, L(0, L(8)))
    assert s.addTwoNumbers(L(3), L(8)) == L(1, L(1))
    assert s.addTwoNumbers(L(3), L(0)) == L(3)
