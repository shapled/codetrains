package main

import "fmt"

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func NewTreeNode(data []int) *TreeNode {
	if len(data) == 0 {
		return nil
	}
	nodes := []*TreeNode{&TreeNode{data[0], nil, nil}}
	for i:=1; i<len(data); i++ {
		if data[i] == 0 {  // 替代 nil，int 数组里面不好加 nil
			nodes = append(nodes, nil)
			continue
		}
		parent := nodes[(i-1)/2]
		if i % 2 == 1 {
			parent.Left = &TreeNode{data[i], nil, nil}
			nodes = append(nodes, parent.Left)
		} else {
			parent.Right = &TreeNode{data[i], nil, nil}
			nodes = append(nodes, parent.Right)
		}
	}
	return nodes[0]
}

func (tn *TreeNode) MiddleOrder() []int {
	c := make(chan *TreeNode, 1)
	var F func(*TreeNode)
	F = func (root *TreeNode) {
		if root.Left != nil {
			F(root.Left)
		}
		c <- root
		if root.Right != nil {
			F(root.Right)
		}
	}
	go func() {
		F(tn)
		close(c)
	}()
	var r []int
	for v := range c {
		r = append(r, v.Val)
	}
	return r
}

func assertEqual(a, b interface{}) {
	if a != b {
		panic(fmt.Sprintf("%#v != %#v", a, b))
	}
}

func assertIntSliceEqual(a, b []int) {
	if len(a) != len(b) {
		panic(fmt.Sprintf("%#v != %#v", a, b))
	}
	for i, v := range a {
		if v != b[i] {
			panic(fmt.Sprintf("%#v != %#v", a, b))
		}
	}
}