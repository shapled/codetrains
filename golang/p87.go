package main

import "fmt"

type SetCount map[rune]int8

func NewSet() *SetCount {
	s := SetCount(make(map[rune]int8))
	return &s
}

func (set *SetCount) CombineString(s string) *SetCount {
	for _, ch := range s {
		cnt, ok := (*set)[ch]
		if ok {
			(*set)[ch] = cnt + 1
		} else {
			(*set)[ch] = 1
		}
	}
	return set
}

func (set *SetCount) ContainsRune(ch rune) bool {
	_, ok := (*set)[ch]
	if ok {
		return true
	}
	return false
}

func (set *SetCount) Length() int {
	return len(*set)
}

func (set *SetCount) Equals(set2 *SetCount) bool {
	if set.Length() != set2.Length() {
		return false
	}
	for key := range *set {
		_, ok := (*set2)[key]
		if !ok || (*set)[key] != (*set2)[key]{
			return false
		}
	}
	return true
}

// 关键还是判断每个节点的二叉是否可以对应上
func isScramble(s1 string, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}
	if len(s1) == 0 {
		return true
	}
	if len(s1) == 1 {
		return s1[0] == s2[0]
	}
	for i:=1; i<len(s1); i++ {
		set11 := NewSet().CombineString(s1[:i])
		set12 := NewSet().CombineString(s1[i:])
		set21 := NewSet().CombineString(s2[:i])
		set22 := NewSet().CombineString(s2[i:])
		if set11.Equals(set21) && set12.Equals(set22) {
			if isScramble(s1[:i], s2[:i]) && isScramble(s1[i:], s2[i:]) {
				return true
			}
		}
		set31 := NewSet().CombineString(s2[len(s1)-i:])
		set32 := NewSet().CombineString(s2[:len(s1)-i])
		if set11.Equals(set31) && set12.Equals(set32) {
			if isScramble(s1[:i], s2[len(s1)-i:]) && isScramble(s1[i:], s2[:len(s1)-i]) {
				return true
			}
		}
	}
	return false
}

func assertEqual(a, b interface{}) {
	if a != b {
		panic(fmt.Sprintf("%#v != %#v", a, b))
	}
}

func main() {
	// error
	assertEqual(isScramble("abb", "bab"), true)

	assertEqual(isScramble("", ""), true)
	assertEqual(isScramble("a", "ab"), false)
	assertEqual(isScramble("a", "a"), true)
	assertEqual(isScramble("ab", "ba"), true)
	assertEqual(isScramble("aca", "caa"), true)
	assertEqual(isScramble("great", "rgeat"), true)
	assertEqual(isScramble("abcde", "caebd"), false)
}
