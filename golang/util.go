package main

import "fmt"

func assertEqual(a, b interface{}) {
	if a != b {
		panic(fmt.Sprintf("%#v != %#v", a, b))
	}
}
