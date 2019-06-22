package main

func TreeElements(c chan *TreeNode, root *TreeNode) {
	if root.Left != nil {
		TreeElements(c, root.Left)
	}
	c <- root
	if root.Right != nil {
		TreeElements(c, root.Right)
	}
}

func recoverTree(root *TreeNode)  {
	c := make(chan *TreeNode, 1)
	go func() {
		TreeElements(c, root)
		close(c)
	}()
	var e1 *TreeNode = nil
	var e2 *TreeNode = nil
	var last *TreeNode = nil
	for node := range c {
		if last != nil && last.Val > node.Val {
			if e1 == nil {
				e1 = last
				e2 = node
			} else {
				e2 = node
			}
		}
		last = node
	}
	e1.Val, e2.Val = e2.Val, e1.Val
}

func main() {
	tree1 := NewTreeNode([]int{1, 3, 0, 0, 2})
	recoverTree(tree1)
	assertIntSliceEqual(tree1.MiddleOrder(), []int{1, 2, 3})
	tree2 := NewTreeNode([]int{3, 1, 4, 0, 0, 2})
	recoverTree(tree2)
	assertIntSliceEqual(tree2.MiddleOrder(), []int{1, 2, 3, 4})
}
