# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x, nxt=None):
        self.val = x
        self.next = nxt


class Solution:

    def reverse(self, start: ListNode):
        if not start or not start.next:
            return start, start
        p1, p2, p3 = start, start.next, start.next.next
        p2.next = p1
        while p3:
            p1, p2, p3 = p2, p3, p3.next
            p2.next = p1
        return p2, start

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        cnt = 0
        changed = False
        last_end = None
        p = group = ret = head
        while p:
            cnt += 1
            last = p
            p = p.next
            if (cnt % k) == 0:
                last.next = None
                start, end = self.reverse(group)
                if not changed:
                    changed = True
                    ret = start
                else:
                    last_end.next = start
                end.next = group = p
                last_end = end
        return ret


def flatten(n: ListNode):
    l = []
    while n:
        l.append(n.val)
        n = n.next
    return l


if __name__ == '__main__':
    s = Solution()
    L = ListNode
    assert flatten(s.reverseKGroup(L(1), 2)) == [1]

    assert flatten(s.reverseKGroup(L(1, L(2, L(3, L(4, L(5))))), 1)) == [1, 2, 3, 4, 5]
    assert flatten(s.reverseKGroup(L(1, L(2, L(3, L(4, L(5))))), 2)) == [2, 1, 4, 3, 5]
    assert flatten(s.reverseKGroup(L(1, L(2, L(3, L(4, L(5))))), 3)) == [3, 2, 1, 4, 5]
    assert flatten(s.reverseKGroup(None, 4)) == []
