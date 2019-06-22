package main

func PostOrderTraversal(c chan int, root *TreeNode) {
	if root.Left != nil {
		PostOrderTraversal(c, root.Left)
	}
	if root.Right != nil {
		PostOrderTraversal(c, root.Right)
	}
	c <- root.Val
}

func postorderTraversal(root *TreeNode) []int {
	if root == nil {
		return []int{}
	}
	c := make(chan int, 1)
	go func() {
		PostOrderTraversal(c, root)
		close(c)
	}()
	result := []int{}
	for value := range c {
		result = append(result, value)
	}
	return result
}

func main() {
	// error
	assertIntSliceEqual(postorderTraversal(NewTreeNode([]int{})), []int{})

	assertIntSliceEqual(postorderTraversal(NewTreeNode([]int{1})), []int{1})
	assertIntSliceEqual(postorderTraversal(NewTreeNode([]int{1, 0, 2, 0, 0, 3})), []int{3, 2, 1})
	assertIntSliceEqual(
		postorderTraversal(NewTreeNode([]int{1, 7, 2, 8, 9, 3})),
		[]int{8, 9, 7, 3, 2, 1},
	)
}
