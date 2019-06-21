# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:

    def DFS(self, node: TreeNode) -> (int, int):
        """ return path_v, max_v """
        path_solution = [node.val]
        max_solution = []
        left_v = right_v = None
        if node.left is not None:
            left_v, left_max_v = self.DFS(node.left)
            path_solution.append(left_v + node.val)
            max_solution.append(left_max_v)
        if node.right is not None:
            right_v, right_max_v = self.DFS(node.right)
            path_solution.append(right_v + node.val)
            max_solution.append(right_max_v)
        if left_v is not None and right_v is not None:
            max_solution.append(left_v + node.val + right_v)
        path_v = max(path_solution)
        max_solution.append(path_v)
        max_v = max(max_solution)
        return path_v, max_v

    def maxPathSum(self, root: TreeNode) -> int:
        _, v = self.DFS(root)
        return v


if __name__ == '__main__':
    s = Solution()
    T = TreeNode
    # error
    assert s.maxPathSum(T(-3)) == -3
    # mine
    assert s.maxPathSum(T(1, T(2), T(3))) == 6
    assert s.maxPathSum(T(-10, T(9), T(20, T(15), T(7)))) == 42
    assert s.maxPathSum(T(3)) == 3
    assert s.maxPathSum(T(3, T(-1), T(-2))) == 3
    assert s.maxPathSum(T(0, T(0, T(3)), T(-1, None, T(2)))) == 4
    assert s.maxPathSum(T(0, T(0, T(3)), T(-2, None, T(1)))) == 3
